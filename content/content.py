import os
import shutil
import gdown
import subprocess
import gc

# Function to download and extract files
def download_and_extract(url, output_zip, output_folder):
    print(f"Downloading {output_zip}...")
    gdown.download(url, output=output_zip, fuzzy=True)
    
    print(f"Extracting {output_zip}...")
    shutil.unpack_archive(output_zip, output_folder)
    os.remove(output_zip)

# Delete and redownload assets
download_and_extract(
    "https://drive.google.com/file/d/1F2MJQ5enUPVtyi3s410PUuv8LiWr8qCz/view?usp=sharing", 
    "assets.zip", 
    "assets")

# Delete and redownload attacks
download_and_extract(
    "https://drive.google.com/file/d/1LAOL8sYCUfsCk3TEA3vvyJCLSl0EdwYB/view?usp=sharing", 
    "attacks.zip", 
    "attacks")

# Free memory
gc.collect()