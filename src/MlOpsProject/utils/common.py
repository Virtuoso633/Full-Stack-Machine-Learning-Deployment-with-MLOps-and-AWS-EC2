# What is utils??
# Those functionality that you would be using frequently in your code instead of writing them everytime in component just keep it in utils file and whenever you need it just call from here..


import os
from box.exceptions import BoxValueError
import yaml
from MlOpsProject import logger
import json
import joblib
from ensure import ensure_annotations #can be used to ensure that all function annotations are properly evaluated
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        if not os.path.exists(path_to_yaml):
            logger.error(f"YAML file: {path_to_yaml} does not exist.")
            raise FileNotFoundError(f"File not found: {path_to_yaml}")

        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)

            # Validate content is a dictionary or list
            if not isinstance(content, (dict, list)):
                logger.error(f"YAML file: {path_to_yaml} contains invalid content for ConfigBox.")
                raise BoxValueError(f"Invalid content format in {path_to_yaml}. Expected dict or list.")

            logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)

    except BoxValueError as bve:
        logger.error(f"BoxValueError: Cannot extrapolate Box from content of the file: {path_to_yaml}. {bve}")
        raise bve

    except Exception as e:
        logger.error(f"An error occurred while reading YAML file: {path_to_yaml}. Error: {e}")
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
