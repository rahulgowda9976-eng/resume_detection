import os
import json

def ensure_directory_exists(file_path: str):
    """Ensure the directory for the given file path exists."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def save_json(data: dict, file_path: str):
    """Save data to a JSON file, ensuring the directory exists."""
    ensure_directory_exists(file_path)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error saving JSON file: {e}")
