import json
import platform
import subprocess
import os

from pathlib import Path
from src.utils.directory import install_ollama_model

path = Path(__file__).cwd() / "config.json"
path_default_config = Path(__file__).cwd() / "default_config.json"

def ensure_config():
  
  current_os = platform.system()


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
    if current_os == "Windows":
      initial_directory = "C://"
      subprocess.run("irm https://ollama.com/install.ps1 | iex", shell=True)
    elif current_os == "Darwin" or "Linux":
      initial_directory = "/"
      subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True)
    else:
      initial_directory = "Not found"

    install_ollama_model("llama3.1:8b")

    
    with open(path_default_config, "w", encoding="utf-8") as file:
      json.dump(default_config, file, ensure_ascii=False, indent=4)
    
    with open(path, "w", encoding="utf-8") as file:
      json.dump(default_config, file, ensure_ascii=False, indent=4)
