from pathlib import Path
import os
from src.utils.get_config import get_config

def load_directory():
    """Retorna o diretório raiz do projeto."""
    return Path(__file__).resolve().parent.parent.parent

def search_path_file(name_file, initial_directory):
    """Busca um arquivo pelo nome em tod o computador"""

    ignore_list = get_config("settings", "ignore_dirs")
    local_directory = os.getcwd()

    for s, d, f in os.walk(local_directory):
        if name_file in f:
            return os.path.join(s, name_file)

    for source, directory, files in os.walk(initial_directory):
        directory[:] = [d for d in directory if d not in ignore_list]
        if name_file in files:

            """os.path.join junta a pasta aual com o nome do arquivo""" 
            return os.path.join(source, name_file)
    return "Arquivo não encontrado"
