#Step 1: Import the required Modules
import requests
import os
import shutil
from datetime import datetime

# Step 2: Clean Up Previous Directory
# Check to see if the directory 'michael_oppong' already exists. 
# If it exist, remove it using 'shutil.rmtree()' to ensure fresh start


if os.path.exists('michael_oppong'):
    try:
        shutil.rmtree('michael_oppong')
        print(f"Directory'{'michael_oppong'}'has been removed successfully")
         
    except Exception as e:
        print(f"Error: {e}")

#Step 3: Create a new directory michael_oppong
download_folder = 'michael_oppong'

if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Directory: {download_folder} created")

# Step 4: Define the Local file Path
# Set the local file path for the file that will be downloaded, and combine
# the directory name with the desired file name

local_file_path = os.path.join(download_folder,'michael_oppong.txt')

# Step 5: Download the file

url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)


if response.status_code == 200:
    print("file successfully downloaded")
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
        print("file saved successfully!")
else:
    print(f"Failed to download the file. The status code: {response.status_code}")


#Step 6: Overwrite File Content
# Receive prompt from the user to overwrite the downloaded file with
# this new content appending a timestamp to indicate when the file was
# last modified
# 
user_input = input("Describe what you have learned so far in a sentence:")
now= datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# with open(local_file_path, "w") as file:
#     file.write(user_input + "\n")
#     file.write(f"last modifed on: {current_time}")
#     print("File successfully modified.")


#Step 7: Display the Updated File content

with open(local_file_path, "r") as file:
    print("\nYou entered: ", end='')
    print(file.read())