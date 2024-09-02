# through this python script every time I execute it, I can create this kind of folder structure..

"""
The template.py file in a project typically serves one or more of the following purposes:

1. Template for New Modules/Files: It can be used as a base template for creating new Python files in the project. This ensures consistency in structure and style across different modules.

2. Code Skeleton: It may provide a skeleton of code with predefined functions, classes, and comments. Developers can fill in the details as per their specific requirements.

3. Example Usage: It can include example usage of functions, classes, or the project itself. This helps new developers understand how to use the project's components.

4. Configuration Template: Sometimes, it might contain a template for configuration settings or parameters that need to be customized for different environments or use cases.

5. Documentation: It may serve as a reference with detailed comments explaining the structure, purpose, and usage of different parts of the project.

"""


# importing some libraries
import os
from pathlib import Path
import logging

# Initialising logging stream . Why? Because, I want to see Path in terminal..

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
# it is information level log, i.e it will save the timestamp i.e the time at which it executed and the error message or successful execution message 

project_name = "MlOpsProject"

# so bacically it will create a folder called src/MlOpsProject/allmycomponents (read as == a/b : b inside a)



"""To make a folder a Python package, you need an __init__.py file in that folder. 
This allows you to import modules from that folder as a package. """
"""
src/
└── your_project_name/
    ├── __init__.py
    ├── config/
    │   ├── __init__.py
    │   └── configuration.py
    └── other_modules/
        ├── __init__.py
        └── other_file.py

"""


'''
The script combines these static and dynamic paths to create the necessary directory structure for the project. 
The project_name variable allows for flexibility in creating paths specific to different projects, 
making the script reusable across various projects with different names.
'''
list_of_files = [
    ".github/workflows/.gitkeep",# folder structure I need every time ### static paths
    f"src/{project_name}/__init__.py", # every time i will need this constructor file to make this folder as my local package , because every time I need to import something from the allmycomponents(components,utils,pipline,entity..) folder.
    f"src/{project_name}/components/__init__.py",## these are dynamic file paths :: These paths contain a variable (project_name) that will change based on the specific project.
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # These are the files I need every time ### static paths
    "params.yaml",## these below are static paths :::These paths are fixed and do not change regardless of the project name or any other variable. They are constant and can be directly used.
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) #Converts the filepath to a Path object.
    filedir, filename = os.path.split(filepath) # for example here I splited my filepath in foldername and filename


    if filedir !="": #Checks if there is a directory path.
        os.makedirs(filedir, exist_ok=True) #Creates the directory if it doesn't exist. The exist_ok=True parameter avoids raising an error if the directory already exists.
        logging.info(f"Creating directory; {filedir} for the file: {filename}") #Logs the creation of the directory.
        ##Tracking Execution: Helps developers track which directories were created and when.
        ##Debugging: If there is an issue with directory creation, the logs can provide clues about what went wrong.
        ##Auditing: Provides an audit trail of the directory creation process, which can be useful for both debugging and compliance purposes.

        '''
        Audit Trail
        Security Auditing: Logs can be used to track security-related events, such as login attempts, access to sensitive data, and configuration changes.
        Compliance: In some industries, maintaining logs is necessary to comply with regulatory requirements.
        '''



    """
    Check if the File Exists and its Size:
    
    not os.path.exists(filepath): Checks if the file does not exist.
    os.path.getsize(filepath) == 0: Checks if the file exists but is empty (size is 0 bytes).
    """
    '''
    Create the File:
    
    with open(filepath, "w") as f:: Opens the file in write mode, creating it if it doesn't exist. The with statement ensures the file is properly closed after the operation.
    pass: This is a placeholder statement indicating no action is taken after opening the file. The file is created and immediately closed.
    logging.info(f"Creating empty file: {filepath}"): Logs that an empty file has been created.
    '''
    
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


        '''
        File Already Exists:
        
        else:: If the file exists and is not empty, this block is executed.
        logging.info(f"{filename} already exists"): Logs that the file already exists.
        '''
    else:
        logging.info(f"{filename} is already exists")
        
    
"""
Summary::

The script ensures that all necessary directories are created.
It checks if each file in the list exists or if it is empty.
If a file does not exist or is empty, it creates an empty file.
It logs the creation of directories and files, as well as the existence of pre-existing files.
This approach ensures that your project structure is set up correctly every time the script is run, without overwriting any existing files that contain data.

"""
