import gymnasium
import camera
from camera import CameraResolution
import save
from save import OpponentsCfg

class SelfPlayWarehouseBrawl(gymnasium.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self,
                 reward_manager: Optional[RewardManager]=None,
                 opponent_cfg: OpponentsCfg=OpponentsCfg(),
                 save_handler: Optional[SaveHandler]=None,
                 render_every: int | None = None,
                 resolution: CameraResolution=CameraResolution.LOW):
        """
        Initializes the environment.

        Args:
            reward_manager (Optional[RewardManager]): Reward manager.
            opponent_cfg (OpponentCfg): Configuration for opponents.
            save_handler (SaveHandler): Configuration for self-play.
            render_every (int | None): Number of steps between a demo render (None if no rendering).
        """
        super().__init__()

        self.reward_manager = reward_manager
        self.save_handler = save_handler
        self.opponent_cfg = opponent_cfg
        self.render_every = render_every
        self.resolution = resolution

        self.games_done = 0


        # Give OpponentCfg references, and normalize probabilities
        self.opponent_cfg.env = self
        self.opponent_cfg.validate_probabilities()

        # Check if using self-play
        if (selfplay_data := self.opponent_cfg.opponents.get('self_play')) is not None:
            assert self.save_handler is not None, "Save handler must be specified for self-play"

            # Give SelfPlayHandler references
            selfplay_handler: SelfPlayHandler = selfplay_data[1]
            selfplay_handler.save_handler = self.save_handler
            selfplay_handler.env = self

        self.raw_env = WarehouseBrawl(resolution=resolution)
        self.action_space = self.raw_env.action_space
        self.act_helper = self.raw_env.act_helper
        self.observation_space = self.raw_env.observation_space
        self.obs_helper = self.raw_env.obs_helper

    def on_training_start(self):
        # Update SaveHandler
        if self.save_handler is not None:
            self.save_handler.update_info()

    def on_training_end(self):
        if self.save_handler is not None:
            self.save_handler.agent.update_num_timesteps(self.save_handler.num_timesteps)
            self.save_handler.save_agent()

    def step(self, action):

        full_action = {
            0: action,
            1: self.opponent_agent.predict(self.opponent_obs),
        }

        observations, rewards, terminated, truncated, info = self.raw_env.step(full_action)

        if self.save_handler is not None:
            self.save_handler.process()

        if self.reward_manager is None:
            reward = rewards[0]
        else:
            reward = self.reward_manager.process(self.raw_env, 1 / 30.0)

        return observations[0], reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        # Reset MalachiteEnv
        observations, info = self.raw_env.reset()

        self.reward_manager.reset()

        # Select agent
        new_agent: Agent = self.opponent_cfg.on_env_reset()
        if new_agent is not None:
            self.opponent_agent: Agent = new_agent
        self.opponent_obs = observations[1]


        self.games_done += 1
        #if self.games_done % self.render_every == 0:
            #self.render_out_video()

        return observations[0], info

    def render(self):
        img = self.raw_env.render()
        return img

    def close(self):
        pass