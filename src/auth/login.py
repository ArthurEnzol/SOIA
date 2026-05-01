import bcrypt
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data" / "passwords"
DATA_FILE = DATA_DIR / "data.txt"

def ensure_data_dir():
    """Garante que o diretório de dados existe."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def login(password: str) -> bool:
    """Verifica a senha contra o hash armazenado."""
    try:
        ensure_data_dir()
        if not DATA_FILE.exists():
            return False
            
        with open(DATA_FILE, "r") as f:
            stored_hash = f.read().strip()
        
        password_bytes = password.encode("utf-8")
        return bcrypt.checkpw(password_bytes, stored_hash.encode("utf-8"))
        
    except Exception as e:
        print(f"Erro no login: {e}")
        return False
