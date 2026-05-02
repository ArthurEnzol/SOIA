import json
import os
from pathlib import Path
import platform

def get_config(set: str, set_: str, modified):

    directory_json = Path(__file__).parent.parent.parent.resolve() / "config.json"

    with directory_json.open("r") as file:
        data = json.load(file)
    
    data["set"]["set_"] = modified

    with directory_json.open("w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

print(os.getcwd() + "\n" , os.getcwdb)