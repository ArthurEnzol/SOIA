from src.ui.menu_config import menu_config_func
from InquirerPy import prompt
from time import sleep
import sys
import os
import platform
import psutil
import threading
import socket
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

from src.ui.display import animation_creating
from src.utils.project_builder import frontend_base, frontend_react, frontend_nextjs, frontend_typescript
from src.ui.terminal import clear_lines

def system_info():
    console = Console()
    stop_monitoring = threading.Event()

    def get_system_info():
        return {
            "Sistema Operacional": platform.system(),
            "Versão do SO": platform.version(),
            "Arquitetura": platform.machine(),
            "Hostname": socket.gethostname(),
            "Núcleos de CPU": psutil.cpu_count(logical=False),
            "Núcleos Lógicos": psutil.cpu_count(logical=True),
            "Uso de CPU (%)": f"[bold green]{psutil.cpu_percent(interval=1):.1f}[/]",
            "Memória Total (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
            "Memória Usada (GB)": round(psutil.virtual_memory().used / (1024**3), 2),
            "Uso de Memória (%)": f"[bold green]{psutil.virtual_memory().percent:.1f}[/]",
        }

    def generate_table():
        sys_info = get_system_info()
        table = Table(
            "Informação", "Valor",
            title="Informações do Sistema",
            caption="Pressione Enter para parar",
            box=box.ROUNDED,
            border_style="bright_blue"
        )
        for key, value in sys_info.items():
            table.add_row(key, str(value))
        return table

    def wait_for_enter():
        input()
        stop_monitoring.set()

    threading.Thread(target=wait_for_enter, daemon=True).start()

    with Live(generate_table(), console=console, refresh_per_second=1) as live:
        while not stop_monitoring.is_set():
            live.update(generate_table())
    clear_lines(18)
    return


def project_builer_menu():
    
    def path_name():
        path = input("Diretorio: ")
        if not path:
            path = os.getcwd
        return path
    
    questions = [
        {
            "type": "list",
            "message": "Selecione sua estrutura de projeto",
            "choices": ["Front-End", "Back-End", "Full-Stack"]
        }
    ]
    
    questions_frontend = [
        {
            "type": "list",
            "message": "Selecione a tecnologia",
            "choices": ["Base", "React", "TypeScript", "NextJs"]
        }
    ]
    
    option = prompt(questions)
    
    match option[0]:
        case "Front-End":
            option_frontend = prompt(questions_frontend)
            
            match option_frontend[0]:
                
                case "Base":
                    path = path_name()
                    frontend_base(path)
                    animation_creating()
                    clear_lines(5)
                case "React":
                    path = path_name()
                    frontend_react(path)
                    animation_creating()
                    clear_lines(5)
                case "TypeScript":
                    path = path_name()
                    frontend_typescript(path)
                    animation_creating()
                    clear_lines(5)
                case "NextJs":
                    path = path_name()
                    frontend_nextjs(path)
                    animation_creating()
                    clear_lines(5)
            
                    

def menu_area():
    """Menu de área logada (após autenticação)."""
    menu_config = [
        {
            "type": "list",
            "message": "Área do Usuário - Selecione uma opção:",
            "choices": ["Machine Perfil", "Project Builder","Configurações", "Sair"]
        }
    ]
    
    option = prompt(menu_config)
    
    if option[0] == "Machine Perfil":
        system_info()
    elif option[0] == "Configurações":
        clear_lines(1)
        menu_config_func()
    elif option[0] == "Sair":
        for x in range(4):
            print("\rSaindo" + "."*x, end="", flush=True)
            sleep(0.3)
            """print("\rSaindo", end="", flush=True)"""
        clear_lines(1)
        
        return False
    elif option[0] == "Project Builder":
        project_builer_menu()
    
    return True
