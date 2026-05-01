from InquirerPy import prompt
import os
import json
from pathlib import Path

questions = [
  {
    "type": "list",
    "message": "Selecione uma opção:",
    "choices": ["Open Json Config"]
  }
]


def json_config():
  path_config_json = Path(__file__).parent.parent.parent / "config.json"
  os.system(f"notepad {path_config_json}")
  
def json_config_reset():
  path_config_json = Path(__file__).parent.parent.parent / "config.json"
  path_default_config_json = Path(__file__).parent.parent.parent / "default_config.json"
  with open(path_default_config_json, "r") as f_origin, open(path_config_json, "w") as f_destin:
    data = json.load(f_origin)
    json.dump(data, f_destin, ensure_ascii=False, indent=4)
    
  

def menu_config_func():
  option = prompt(questions)
  if option[0] == "Open Json Config":
    json_config()
    