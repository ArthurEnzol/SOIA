import bcrypt
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data" / "passwords"
DATA_FILE = DATA_DIR / "data.txt"

def ensure_data_dir():
    """Garante que o diretório de dados existe."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def hash_password(password: str) -> str:
    """Retorna o hash bcrypt da senha."""
    password_bytes = password.strip().encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")

def save_password(password: str) -> bool:
    """Salva o hash da senha no arquivo de dados."""
    try:
        ensure_data_dir()
        hashed = hash_password(password)
        
        with open(DATA_FILE, "w") as f:
            f.write(hashed)
        return True
        
    except Exception as e:
        print(f"Erro ao salvar senha: {e}")
        return False

def verify_password(password: str, hashed: str) -> bool:
    """Verifica se a senha corresponde ao hash."""
    password_bytes = password.strip().encode("utf-8")
    hashed_bytes = hashed.strip().encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)
