import os
import subprocess
import shutil

# Function to restart a service
def restart_service(service_name):
	try:
		subprocess.run(['sudo', 'systemctl','restart', service_name],check=True)
		print(f"Service '{service_name}' restarted successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Error restarting serive '{service_name}': {e}")

# Function to create a new temp folder by deleting existing ones
def clear_temp_folder(temp_folder):
	try:
		shutil.rmtree(temp_folder)
		os.makedirs(temp_folder)
		print(f"Temporary folder '{temp_folder}'cleared successfully.")
	except Exception as e:
		print(f"Error clearing emprorary fodler '{temp_folder}': {e}")

if __name__  == "__main__":
	SERVICE_NAME = "cron" # Replace with your service name
	TEMP_FOLDER  = "/home/michael/cron_jobs/temp_folder" # Replace with your tem folder path
	
	restart_service(SERVICE_NAME)
	clear_temp_folder(TEMP_FOLDER)
