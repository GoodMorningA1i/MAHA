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

## Environemnt Setup ##
cd environment

# Low High Class
python3.10 action_space_helper.py
python3.10 observation_space_helper.py
python3.10 key_icon_panel.py
python3.10 ui_handler.py
python3.10 camera.py
python3.10 warehouse_brawl_env.py

cd ..