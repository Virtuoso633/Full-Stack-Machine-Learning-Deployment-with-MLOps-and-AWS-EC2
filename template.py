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
from pathlib import Path #
import logging

# Initialising logging stream . Why? Because, I want to see Path in terminal..

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
# it is information level log, w.r.t it will save the timestamp i.e the time at which it executed and the error message or successful execution message 

project_name = "MlOpsProject"

# so bacically it will create a folder called src/MlOpsProject/allmycomponents (read as == a/b : b inside a)

list_of_files = [
    ".github/workflows/.gitkeep",# folder structure I need every time
    f"src/{project_name}/__init__.py", # every time i will need this constructor file to make this folder as my local package , because every time I need to import something from the parent components folder.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # These are the files I need every time
    "params.yaml",
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
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")

