import json
import platform
from pathlib import Path

path = Path(__file__).cwd() / "config.json"
path_default_config = Path(__file__).cwd() / "default_config.json"

def ensure_config():
  
  current_os = platform.system()

  if current_os == "Windows":
    initial_directory = "C://"
  elif current_os == "Darwin" or "Linux":
    initial_directory = "/"
  else:
    initial_directory = "Not found"

  if not path.exists() and not path_default_config.exists():
    default_config = {
      "settings":  {
        "system": current_os,
        "language": "pt-br"
      },
      "commands": {
        "env_name": "venv",
        "initial_directory": initial_directory
      },
      "git": {
        "default_branch": "main",
        "auto_add_all": False
      }
    }

    
    with open(path_default_config, "w", encoding="utf-8") as file:
      json.dump(default_config, file, ensure_ascii=False, indent=4)
    
    with open(path, "w", encoding="utf-8") as file:
      json.dump(default_config, file, ensure_ascii=False, indent=4)
