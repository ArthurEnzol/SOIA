import sys

def clear_lines(lines: int):
    """Limpa N linhas do terminal."""
    for _ in range(lines):
        sys.stdout.write('\033[A')
        sys.stdout.write('\033[2K')
    sys.stdout.flush()
    
