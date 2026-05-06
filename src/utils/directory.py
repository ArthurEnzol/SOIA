from pathlib import Path
import os
import requests
from tqdm import tqdm
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

def install_ollama_model(modelo):
    url = "http://localhost:11434/api/pull"
    payload = {"name": modelo, "stream": True}

    try:
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            barra = None
            for linha in response.iter_lines():
                if linha:
                    dado = linha.decode('utf-8')
                    if dado.startswith("data:"):
                        info = dado[5:].strip()
                        try:
                            import json
                            dados_json = json.loads(info)
                            status = dados_json.get("status", "")
                            print(f"[Ollama] {status}")

                            # Atualiza barra de progresso se estiver baixando
                            if "downloading" in status.lower():
                                total = dados_json.get("total", 1)
                                concluido = dados_json.get("completed", 0)
                                if barra is None:
                                    barra = tqdm(total=total, unit="B", unit_scale=True, desc="Download")
                                barra.update(concluido - barra.n)
                            elif "pulling" in status.lower():
                                print(status)
                        except json.JSONDecodeError:
                            pass
            if barra:
                barra.close()
            print("Modelo instalado com sucesso!")
    except requests.exceptions.ConnectionError:
        print("Error: Ollama não está rodando. Execute 'ollama serve' primeiro.")
    except Exception as e:
        print(f"Error: {e}")