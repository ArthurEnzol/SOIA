from pathlib import Path

def load_directory():
    """Retorna o diretório raiz do projeto."""
    return Path(__file__).resolve().parent.parent.parent
