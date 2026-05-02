import os
import sys
from pathlib import Path

import typer
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
def config(reset: bool = typer.Option(False, "--reset", help="Reset your configs")):
    
    '''
        Open the user settings (JSON) 
    '''
    
    if reset:
        json_config_reset()
    else:
        json_config()

@app.command()
def git(
    init: bool = typer.Option(False, "--init", "-i"),
    add: str = typer.Option(".", "--add", "-a"),
    commit: str = typer.Option("Update", "--commit", "-c"),
    push: bool = typer.Option(False, "--push", "-p"),
    branch: str = typer.Option("main", "--branch", "-b"),
    status: bool = typer.Option(False, "--status", "-s"),
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
        os.system(f'git push origin "{branch}"')
    if branch:
        os.system(f'git branch {branch}')
    if status:
        os.system(f'git status')

@app.command()
def path():
    '''
        Mostra o diretório de trabalho atual (cwd) e a pasta raiz do SOIA.
        Caminhos absolutos e resolvidos — compatível com Linux, macOS e Windows.
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
    flags: bool = typer.Option(False, "--flags"),
         ):
    if flags:
        help_flags_cli()
        return

    
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