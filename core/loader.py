import yaml
import os

def load_yaml(path: str) -> dict:
    """
    Loads and parses a YAML file.

    Args:
        path (str): Path to the YAML file.

    Returns:
        dict: Parsed YAML data as a Python dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If there's a parsing error.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"YAML file not found: {path}")

    with open(path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            if data is None:
                return {}
            return data
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file {path}: {e}")
