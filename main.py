import os
import subprocess

from appdirs import user_data_dir
appname = "RunMyCommand"
appauthor = "YoussefAttai"

def run_command_as_admin(command):
    try:
        subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Handle the error as needed

# Specify the path to the file containing the command
app_data_dir = user_data_dir(appname, appauthor)
file_path = os.path.join(app_data_dir, 'mycommands.txt')

try:
    # Open the file and read the command
    with open(file_path, 'r') as file:
        commands = [line.strip() for line in file.readlines()]

except FileNotFoundError:
    print(f"File not found at {file_path}")
    user_command = input("Enter the command to be saved: ")

    # If the file is not found, create the necessary directories
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save the user's command to the file
    with open(file_path, 'w') as file:
        file.write(user_command)

    print(f"Command saved. If you want to edit the command, you can find it here: {file_path}")

    # Set the command to the user's input
    commands = [user_command]

try:
    # Run the command as administrator
    print(f"Running your commands: {commands}")
    print(f"You can change your commands by editing {file_path}")
    for command in commands:
        run_command_as_admin(command)
except Exception as e:
    print(f"Error: {e}")
