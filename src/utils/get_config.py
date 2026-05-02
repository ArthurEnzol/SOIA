import json
import os
from pathlib import Path
import platform

def get_config(set_one: str, set_two: str, modified=False):

    directory_json = Path(__file__).parent.parent.parent.resolve() / "config.json"

    with directory_json.open("r") as file:
        data = json.load(file)
    
    if modified:
        data[set_one][set_two] = modified
        with directory_json.open("w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    else: 
        return data[set_one][set_two]