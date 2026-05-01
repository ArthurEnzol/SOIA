import ollama
import os
from dotenv import load_dotenv
import json

# Configurações de caminhos
MEMORY_FILE = "soia_memory.json"
COMMANDS_DIR = "commands/scripts"
DOWNLOADS_DIR = "commands/downloads"

# Garante que as pastas existam na raiz do projeto
os.makedirs(COMMANDS_DIR, exist_ok=True)
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

load_dotenv()

# Suas importações existentes
# from src.utils.project_builder import frontend_base, frontend_nextjs, frontend_react, frontend_typescript

def load_existents_scripts():
    if not os.path.exists(COMMANDS_DIR):
        return ""
    scripts = os.listdir(COMMANDS_DIR)
    if not scripts:
        return ""
    skills_list = "\nVocê já possui estes scripts prontos na pasta commands/scripts/:\n"
    for s in scripts:
        skills_list += f"- {s}\n"
    return skills_list

# Prompt do Sistema (Skills)
skills = f"""
Seu nome é Soia
1. Perfil Operacional

    Tom: Técnico, direto e profissional. Sem introduções ou conclusões sociais.

    Ação: Se a tarefa exige ação no sistema, a resposta deve ser um script Python.

2. Regras de Codificação (Obrigatório)

    Tags: Todo código deve estar entre <CODE> e </CODE>.

    Bibliotecas: Prefira a biblioteca padrão (os, sys, shutil, subprocess).

    Robustez: Sempre envolva a lógica principal em um bloco try-except para reportar erros de permissão ou caminho.

3. Gestão de Arquivos e Caminhos

    Scripts de Comando: Salve em {COMMANDS_DIR}/.

    Arquivos/Downloads: Salve em {DOWNLOADS_DIR}/.

    Caminhos Dinâmicos: Nunca use caminhos fixos (hardcoded). Use sempre:

        HOME = os.path.expanduser("~")

        Exemplo para Vídeos: os.path.join(HOME, "Videos")

4. Fluxo de Criação de Projetos

    Validação de Local: Se o usuário pedir para criar uma estrutura/pasta sem especificar o local, pare e pergunte o diretório primeiro.

    Caminhos Absolutos: Use caminhos absolutos para qualquer operação fora das pastas temporárias da Soia.

5. Integração de Contexto

    Consulte scripts existentes em: {load_existents_scripts()} antes de criar novos para evitar duplicidade.

6. Template Padrão de Resposta
<CODE>
import os
def executar():
try:
# Implementação direta
pass
except Exception as e:
print(f"Erro: e")

if name == "main":
executar()
</CODE>
"""

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try: 
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_memory(command, logic, file_name=None):
    # Salva no JSON
    memory = load_memory()
    memory[command] = logic
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)
    
    # Salva o arquivo .py físico se um nome for fornecido
    if file_name:
        path = os.path.join(COMMANDS_DIR, f"{file_name}.py")
        with open(path, 'w') as f:
            f.write(logic)
        return path
    return None

def soia(prompt: str):
    try:
        response = ollama.chat(
            model="qwen3.5:4b",
            messages=[
                {'role': 'system', 'content': skills},
                {'role': 'user', 'content': prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

def execute_dinamic_code(code: str):
    try:
        # Executa o código gerado
        exec(code, globals()) 
        return "Tarefa executada com sucesso"
    except Exception as e:
        return f"Erro na execução: {e}"

# --- LOOP PRINCIPAL ---

def soia_prompt(prompt: str):
  user_input = prompt
  memoria = load_memory()

  # 1. Verifica se já conhece o comando
  if user_input.lower() in memoria:
      print("Soia: Executando...")
      print(execute_dinamic_code(memoria[user_input.lower()]))

  else:
      resposta = soia(user_input)
      
      if "<CODE>" in resposta:
          codigo = resposta.split("<CODE>")[1].split("</CODE>")[0].strip()
          print(f"\n--- SCRIPT GERADO ---\n{codigo}\n---------------------")
          
          confirmar = input("Executar e salvar este novo conhecimento? (s/n): ")
          if confirmar.lower() == 's':
              # Executa
              print(execute_dinamic_code(codigo))
              
              # Define um nome para o arquivo baseado no input ou pede ao usuário
              nome_slug = user_input.lower().replace(" ", "_")[:20]
              caminho = save_memory(user_input.lower(), codigo, file_name=nome_slug)
              
              print(f"Soia: Conhecimento salvo em {caminho} e na memória principal.")
      else:
          print(f"Soia: {resposta}")