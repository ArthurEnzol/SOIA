import os
import sys
from pathlib import Path

import typer
from typing import Optional
from dotenv import load_dotenv


from src.core.constants import SOIA_LOGO
from src.core.loader import load_project
from src.utils.directory import load_directory
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
def git(
    init: bool = typer.Option(None, "--init", "-i", help= "Initialize de git repository"),
    add: Optional[str] = typer.Option(None, "--add", "-a", help= "Add files on commit"),
    commit: Optional[str] = typer.Option(None, "--commit", "-c", help= "Commit"),
    push: bool = typer.Option(None, "--push", "-p", help="Push files to repository"),
    status: bool = typer.Option(None, "--status", "-s", help= "Show the files modified"),
    branch: Optional[str] = typer.Option(None, "--branch", "-b", help= "Select your branch for commit")
):
    '''
        Git commands (init, add, commit, push, branch)
    '''
    if init:
        os.system(f'git init')
    if add:
        os.system(f'git add {add}')
    if commit:
        os.system(f'git commit -m "{commit}"')
    if push:
        remote_branch = branch if branch != None else "main"
        os.system(f'git push origin "{remote_branch}"')
    if branch:
        os.system(f'git branch {branch if branch else "main"}')
    if status:
        os.system(f'git status')
    

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

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
):

    
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