# common fuctionality used in the project

import os
import sys
import yaml
from src.DataScienceProject import logger
import json
import joblib # joblib is used for saving and loading models - serialized formats
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file does not exist or is empty.
        e: empty file
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) # safe_load is used to avoid executing arbitrary code
            logger.info(f"YAML file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file at {path_to_yaml} is empty or does not exist.")
    except Exception as e:
        raise e        
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
        
    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save in the JSON file.
        
    Returns:
        None
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Data saved to JSON file at {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    """
    Loads a dictionary from a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)

    logger.info(f"Data loaded from JSON file at {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        data (Any): Data to save in the binary file.
        
    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved to binary file at {path}")
    return data

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(filename=path)
    logger.info(f"Data loaded from binary file at {path}")
    return data