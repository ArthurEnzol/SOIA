from src.auth.login import login
from src.auth.password_manager import save_password
from src.ui.terminal import clear_lines
from src.utils.get_config import get_config
from time import sleep
from InquirerPy import prompt
import os
import getpass
import subprocess

def show_menu():
    """Exibe o menu principal e retorna a opção selecionada."""
    menu_config = [
        {
            "type": "list",
            "message": "Selecione uma opção"    ,
            "choices": ["Login", "Criar conta", "GitHub", "Suporte"]
        }
    ]
    return prompt(menu_config)

def handle_login():
    """Gerencia o fluxo de login com tentativas limitadas."""
    attempts = 0
    max_attempts = 4
    
    while attempts <= max_attempts:
        password = getpass.getpass("Password: ")
        success = login(password)
        
        if success:
            clear_lines(2)
            return True
        
        attempts += 1
        
        if attempts == 1:
            print(f'\033[32mTentativas: {attempts}\033[0m')
        elif attempts == 2:
            print(f'\033[93mTentativas: {attempts}\033[0m')
        elif attempts == 3:
            print(f'\033[33mTentativas: {attempts}\033[0m')
        elif attempts == 4:
            print(f'\033[91mTentativas: {attempts}\033[0m')
            print('\033[91mÚLTIMA TENTATIVA\033[0m')
            
        if attempts > max_attempts:
            print(f"Tentativas excedidas: {attempts}")
            for i in range(10):
                print(f"\rCronômetro: {i}", end="", flush=True)
                sleep(1)
            return False
            
    return False

def handle_create_account():
    """Gerencia o fluxo de criação de conta."""
    password = getpass.getpass("Digite sua senha: ")
    password_confirm = getpass.getpass("Digite sua senha novamente: ")
    
    if password == password_confirm:
        
        questions = [
            {
                "type": "confirm",
                "message": "Confirmar?"
            }
        ]
        resp = prompt(questions)
        if resp[0] == False:
            print("Cancelando...")
            clear_lines(5)
            return False
        print("Salvando senha...")
        save_password(password)
        sleep(3)
        print("Senha salva com sucesso")
        sleep(1.5)
        clear_lines(6)
        return True
    else:
        print("Digite duas senhas iguais...")
        return False

def menu():
    """Menu principal da aplicação."""
    while True:
        try:
            option = show_menu()
            
            if option[0] == "Login":
                if handle_login():
                    return True
            elif option[0] == "Criar conta":
                if handle_create_account():
                    break
            elif option[0] == "GitHub":
                print("Abrindo GitHub...")
                system = get_config("settings", "system")

                match system:
                    case "Linux":
                        subprocess.run("xdg-open https://github.com/ArthurEnzol/SOIA")
                    case "Windows":
                        subprocess.run("start https://github.com/ArthurEnzol/SOIA")
                    case "Darwin":
                        subprocess.run("open -a 'Google Chrome' https://github.com/ArthurEnzol/SOIA")
                        
                sleep(2.5)
                clear_lines(2)
            elif option[0] == "Suporte":
                print("Contato de suporte: soiaterminalassistent@gmail.com")
                os.system("start mailto:soiaterminalassistent@gmail.com?subject=Suporte")
                sleep(2)
                clear_lines(2)
                
                
        except Exception as e:
            print(f"Erro: {e}")
