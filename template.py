import os
from pathlib import Path
import logging 

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:')

project_name = "DataScienceProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", # pipeline components - data ingestion, preprocessing, model training, etc.
    f"src/{project_name}/utils/__init__.py", # general utility functions-used across the project
    f"src/{project_name}/utils/common.py", # all the common functions used across the project
    f"src/{project_name}/config/__init__.py", # configuration files - 
    f"src/{project_name}/config/configuration.py", # main configuration file
    f"src/{project_name}/pipeline/__init__.py" ,# pipeline will have all the information related to the pipeline - training, testing, validation, etc. and it will all the components folders step by step
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/entity/config_entity.py", # configuration entity - will have all the configuration classes
    f"src/{project_name}/constants/__init__.py", # constants file - will have all the constants used across the project
    "config/config.yaml", # main configuration file
    "params.yaml", # parameters file - will have all the parameters used across the project
    "schema.yaml", # schema file - will have all the schema used across the project
    "main.py", # main file - will have the main function to run the project
    "Dockerfile", # docker file - to create a docker image of the project
    "requirements.txt", # requirements file - to install the dependencies
    "setup.py", # setup file - to install the project as a package
    "research/research.ipynb", # research file - to do the research on the project
    "templates/index.html", # template file - to create the web application - using flask or streamlit
    
]
   
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)  # create directories if they do not exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path} and is not empty.")