from rich.console import Console
import sys
import time

console = Console()

def center_txt(txt: str):
    """Exibe texto centralizado no terminal."""
    console.print(txt, justify='center', style="dark_green")

def animation_creating(texto="Criando", pontos=3, intervalo=0.2):
    # Código ANSI para cor Verde: \033[32m
    # Código ANSI para Resetar cor: \033[0m
    VERDE = "\033[32m"
    RESET = "\033[0m"
    
    sys.stdout.write(f"{VERDE}{texto}")
    sys.stdout.flush()
    
    for _ in range(pontos):
        time.sleep(intervalo)
        sys.stdout.write(".")
        sys.stdout.flush()
    
    print(f"{RESET}")
