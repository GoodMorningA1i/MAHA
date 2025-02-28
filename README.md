# UTMIST $\text{AI}^2$ Tournament 2025

**Team Name:** $\sqrt{\text{AI}^2}$\
**Game:** Simplified Brawhala

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
