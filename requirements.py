import subprocess
import sys
import os

# Path to the virtual environment folder
venv_folder = 'myenv'

# Path to the requirements.txt file
requirements_file = 'requirements.txt'

# Check if the virtual environment exists, if not, create it
if not os.path.exists(venv_folder):
    subprocess.call([sys.executable, '-m', 'myenv', venv_folder])

# Activate the virtual environment
if sys.platform == 'win32':
    venv_python = os.path.join(venv_folder, 'Scripts', 'python.exe')
else:
    venv_python = os.path.join(venv_folder, 'bin', 'python')

# Install the required libraries if they are not already installed
def install_if_missing(package):
    try:
        subprocess.check_output([venv_python, '-m', 'pip', 'show', package])
    except subprocess.CalledProcessError:
        subprocess.call([venv_python, '-m', 'pip', 'install', package])

# Read the requirements.txt file and install missing libraries
with open(requirements_file, 'r') as f:
    for line in f:
        package = line.strip()
        install_if_missing(package)

# Run the rest of your script here
