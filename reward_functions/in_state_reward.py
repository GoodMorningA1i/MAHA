def in_state_reward(
    env: WarehouseBrawl,
    desired_state: Type[PlayerObjectState]=BackDashState,
) -> float:
    # Get player object from the environment
    player: Player = env.objects["player"]

    # Apply reward if the player is in the desired state
    reward = 1 if isinstance(player.state, desired_state) else 0.0

    return reward * env.dt