import os
import platform
import sys
import typer
import subprocess


from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from colorist import ColorHex


from src.utils.get_config import get_config
from src.utils.config_handler import ensure_config
from src.core.constants import SOIA_LOGO
from src.core.loader import load_project
from src.utils.directory import install_ollama_model, load_directory, search_path_file 
from src.ui.display import center_txt
from src.ui.menu import menu
from src.ui.menu_area import menu_area
from src.ui.menu_config import json_config, json_config_reset
from src.utils.cli_commands import create_cli, help_flags_cli
from src.utils.infosystem_cmd import run_infosystem_live
from src.core.soia_IA import soia_prompt


app = typer.Typer()
load_dotenv()    

@app.command()
def config(reset: bool = typer.Option(False, "--reset", "-r", help="Reset your configs")):
    
    '''
        Open the user settings (JSON) 
    '''
    
    if reset:
        json_config_reset()
    else:
        json_config()

@app.command()
def env(
    create: Optional[bool] = typer.Option(False, "--create", "-c", help="Create a virtual eviroment"),
    install: Optional[bool] = typer.Option(False, "--install", "-i", help="Install all project dependeces")
):
    current_os = get_config("settings", "system")
    if create:
        name_env = get_config("commands", "env_name")
        os.system(f"python -m venv .{name_env}")

        if current_os == "Windows":
            os.system(f"{search_path_file(name_env)}/Scripts/activate.bat" )
        elif current_os == "Linux" or "Darwin":
            os.system(f"source {search_path_file(name_env)}/Scripts/activate")
    
    if install:
        local_directory = os.getcwd()

        for source, directory, files in os.walk(local_directory):
            if "requirements.txt" in files:
                os.system("python3 -m pip install -r requirements.txt")
                with open("requirements.txt", "r") as requirements:
                    dependeces = list(line.strip() for line in requirements)
                print(ColorHex("#00ff15"), (f"Dependênias instaladas com sucesso: {" ".join([dep for dep in dependeces])}"))


@app.command()
def git(
    init: bool = typer.Option(None, "--init", "-i", help= "Initialize de git repository"),
    add: Optional[str] = typer.Option(None, "--add", "-a", help= "Add files on commit"),
    commit: Optional[str] = typer.Option(None, "--commit", "-c", help= "Commit"),
    push: bool = typer.Option(None, "--push", "-p", help="Push files to repository"),
    status: bool = typer.Option(None, "--status", "-s", help= "Show the files modified"),
    branch: Optional[str] = typer.Option(None, "--branch", "-b", help= "Select your branch for commit"),
    clone: Optional[str] = typer.Option(None, "--clone", "-cr", help="Clone a GitHub repository")
):
    '''
        Git commands (init, add, commit, push, branch)
    '''
    abs_path = os.getcwd()

    if init:
        subprocess.run(f"cd '{abs_path}'")
        subprocess.run(f'git init')
    if add:
        current_os = get_config("settings", "system")
        if current_os == "Windows":
            initial_directory = "C://"
        else: 
            initial_directory = "/"
        path_file = search_path_file(add, initial_directory)   
        subprocess.run(f"git add '{path_file}'")
    if commit:
        subprocess.run(f'git commit -m "{commit}"')
    if push:
        remote_branch = branch if branch != None else get_config("git", "default_branch")
        subprocess.run(f'git push origin "{remote_branch}"')
    if branch:
        subprocess.run(f'git branch {branch if branch else "main"}')
    if status:
        subprocess.run(f'git status')
    if clone:
        subprocess.run(f"git clone {clone}")
    

@app.command()
def path():
    '''
        Mostra o diretório de trabalho atual (cwd) e a pasta raiz do SOIA.
    '''
    cwd = Path.cwd().resolve()
    root = load_directory().resolve()
    print(f"Diretório atual: {cwd}")
    print(f"Projeto SOIA:   {root}")


@app.command("infosystem")
def infosystem():
    '''
        Painel animado com todas as informações do sistema (atualiza a cada 0,5 s; Enter para sair).
    '''
    run_infosystem_live()


@app.command("system-info")
def system_info_screen():
    '''
        Alias de infosystem: mesmo painel ao vivo com métricas do sistema.
    '''
    run_infosystem_live()


@app.command()
def prompt(
    r: str = typer.Option("default", "-r")
):
    '''
        The IA prompt
    '''

    soia_prompt(r)

@app.command()
def create(
    type: str = typer.Option("default", "--type"),
    tech: str = typer.Option("default", "--tech"),
    path: str = typer.Option(os.getcwd(), "--path")
):
    
    """
        Create a structure project
    """
    
    create_cli(type, tech, path)

@app.command
def install(
    ollama: Optional[bool] = typer.Option(False, "--ollama", "-o", help="Install the Ollama Local AI"),
    webui: Optional[bool] = typer.Option(False, "--webuai", "-w", help="Install the WebUAI")
):
    
    """
        Install the AI dependeces
    """

    system = get_config("settings", "system")
    if install:
        if ollama:
            match system:
                case "Linux":
                    subprocess.run("curl -fsSL https://ollama.com/install.sh | sh")
                case "Darwin":
                    subprocess.run("curl -fsSL https://ollama.com/install.sh | sh")
                case "Windows":
                    subprocess.run("irm https://ollama.com/install.ps1 | iex")
            install_ollama_model("llama3.1:8b")
        if webui:
            match system:
                case "Linux":
                    subprocess.run("docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main")

            

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
):
    ensure_config()



    if ctx.invoked_subcommand is not None:
        return
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    center_txt(SOIA_LOGO)
    load_project(load_directory())

    print(f"Executando de: {sys.executable}")
    print("----------------------------------")
    while True:
        if menu():
            while True:
                if not menu_area():
                    break

    input("\nPressione ENTER para encerrar...")
    

if __name__ == "__main__":
    app()