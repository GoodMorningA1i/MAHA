# UTMIST $\text{AI}^2$ Tournament 2025

**Team Name:** $\sqrt{\text{AI}^2}$\
**Game:** Simplified Brawhala\
**Team members:** Ali Syed, Madhav Ajayamohan (Maddy), Adrian Lau, Hasnain Syed


<img width="708" alt="Screenshot 2025-02-28 at 5 57 13 AM" src="https://github.com/user-attachments/assets/76ad3df7-7ff2-411d-a3a8-a10ea67bb3ed" />



## Purpose

The AI² Tournament is run by the University of Toronto Machine Intelligence Student Team, UTMIST. The tournament centers around designing and training a reinforcement learning agent in a smash-bros style platformer fighting game, inspired from the game Brawhala.

## Our agent

Meet Maha, our fighter! 

We trained it for 1,000,000 timesteps using a variety of reward functions and weights. We also challenged it against a variety of different agents. For example, ConstantAgent, RandomAgent, BasedAgent. 

Maha is based off of the Proximal Policy Optimization (PPO) algorithm. The main idea of the algorithm is that after an update, the new policy should not be too far off from the old policy. PPO leverages clipping to avoid large updates.

## Installation Requirements
At least Python 3.10

## To set up locally

Run `bash setup.sh` in the terminal.

### Virtual Environment
You'll notice that a new env/ folder is created. This is to set up a virtual environment. If you set up a virtual environment, your project will become a self contained application, independent of the system installed Python and its modules.

While we do set up for you and activiate the virtual environment, we thought it would be beneficial for you to know how to activate and deactivate the environment by yourself. 

To activate the virtual environment, run `source env/bin/activate` in the terminal.
To deactivate, run `deactivate`.

## Reward Functions

In order to design the model, we came up with six new reward functions, while modifying two existing reward functions.

### New reward functions

#### Danger Zone Rewards
hori_danger_zone reward: This penalizes the agent for moving too far to the right or left of the stage 
vert_danger_zone reward: This penalizes the agent for moving too close to the ceiling or the ground of the stage

#### Recovery Reward
This reward function is aimed to promote recovery behavior in the agent
What the function does is that:
- If the agent is too far to the right, then it rewards the agent for moving to the left and penalizes it for moving to the right
- If the agent is too far to the left, then it rewards the agent for moving to the right and penalizes it for moving to the left
The same principle is used for vertical movements

#### Dodge Reward
Gives a reward each time we go into a dodge state when the opponent is in an attack state

#### Edgeguarding Rewards
These are rewards functions aimed to promote edgeguarding. We hope that the below rewards, in conjunction with the move_to_opponent function, will promote edge_gaurding
- opponent_offstage_reward: Rewards the agent each time the opposing agent is offstage
- guard_reward: Rewards the agent for being in an attacking state when the opponent is recovering.

### Modified reward functions

#### on_knockout_reward
We modified knockout_reward to reward the agent more the more stocks it takes– e.g. the agent is rewarded more if it takes the opponents second stock then if it takes the first stock. Similarly, we penalized the agent more the more stocks it loses

#### damage_interac_reward
We modified this functions in the following way
- For the first half of the match, the reward is damage dealt - damage taken
- For the second half of the match
  - If the agent has a stock advantage over the opponent, it is only rewarded based on -damage_taken, which aims to promote behavior like guarding the agent’s remaining stock so it can win by timeout
  - If the agent has less stocks, or the same number of stocks, the reward is based on damage_dealt– this wants to promote aggressive behaviour in the agent, and beat the other agent down as soon as possible


## Skills Needed
Python and its packages, APIs, Reinforcement Learning, Git-flow, DevOps and Rulesets, Pull Requests, Linux and Shell Script, Virtual Environments
