## Run this file from the folder where it is located ##

#Virtual environment setup
pip install virtualenv
python3 -m venv env
source env/bin/activate

#Install the required packages
pip install -r requirements.txt

#Patch: To set up content like assets and attacks
cd content
python3 content.py
cd ..

#Malachite (DO NOT MODIFY UNLESS YOU KNOW WHAT YOU'RE DOING)
cd malachite
python3 malachite_env.py
cd ..

# Environment Imports
cd imports
python3.10 env_imports.py
cd ..

## Environemnt Setup ##
cd environment

# Low High Class
python3.10 action_space_helper.py
python3.10 observation_space_helper.py
python3.10 key_icon_panel.py
python3.10 ui_handler.py
python3.10 camera.py
python3.10 warehouse_brawl_env.py
python3.10 other_game_objects.py
python3.10 reward_configuration.py
python3.10 save.py
python3.10 self_play_warehouse_brawl.py
python3.10 run_match.py

cd ..

# Agent Classes
cd agents
python3 agent_classes.py
cd ..

# Submission Imports
cd imports
python3 submission_imports.py
cd ..

# Instantiate Submitted Agent
cd maha
python3 submitted_agent.py
python3 instantiate_submitted_agent.py
cd ..

# UserInputAgent - Playing the game ourselves
cd agents
python3 user_input_agent.py
cd ..