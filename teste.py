import ollama
import os
from dotenv import load_dotenv
import json

MEMORY_FILE = "soia_memory.json"

load_dotenv()

from src.utils.project_builder import frontend_base, frontend_nextjs, frontend_react, frontend_typescript

skills = """
Your name is Soia.
Identity: You are a highly efficient AI assistant create by Arthur.
Personality: 
1. Be direct and concise. Do not use filler words.
2. Be polite but professional (technical etiquette).
3. If asked for your name, identify as Soia.
4. If a task requires system action (creating folders, checking files), use your provided tools.
5. Avoid long introductory sentences like "As an AI model..." or "I can certainly help you with...". Just do the task.
6. SEMPRE que gerar um código para o usuário, use as tags <CODE> e </CODE>.
7. Se o usuário pedir para 'baixar', 'criar' ou 'executar', gere o código Python completo.
8. Não use comandos de terminal puro (como youtube-dl), prefira scripts Python (usando bibliotecas como yt_dlp ou os.system) para que eu possa executar via exec().
"""


def load_memory():
  if os.path.exists(MEMORY_FILE):
    try: 
      with open(MEMORY_FILE, 'r') as f:
        return json.load(f)
    except Exception as e:
      return {}
  return {}

def save_memory(command, logic):
  memory = load_memory()
  memory[command] = logic
  with open(MEMORY_FILE, 'w') as f:
    json.dump(memory, f, indent=2)

def soia(prompt: str):
  try:
    response = ollama.chat(
      model="llama3",
      messages=[
        {
          'role': 'system',
          'content': skills
        },
        {
          'role': 'user',
          'content': prompt
        }
      ]
    )
    return response['message']['content']
  except Exception as e:
    return f"Error: {e}"

def execute_dinamic_code(code: str):
  """Excute the code created by SOIA"""

  try:
    exec(code)
    return "Tarefa executada com sucesso"
  except Exception as e:
    return f"Erro: {e}"

user_input = input("Você: ")

# 1. Verifica se é um comando que ela já "aprendeu" na memória
memoria = load_memory()
if user_input in memoria:
    print("Soia: Executando comando aprendido...")
    execute_dinamic_code(memoria[user_input])
else:
    # 2. Se não conhece, manda para o Ollama
    resposta = soia(user_input)
    
    # 3. Se a resposta contiver código (ex: entre tags <CODE>), você executa
    if "<CODE>" in resposta:
        codigo = resposta.split("<CODE>")[1].split("</CODE>")[0]
        confirmar = input(f"Soia sugeriu esse código:\n{codigo}\nExecutar? (s/n): ")
        if confirmar.lower() == 's':
            print(execute_dinamic_code(codigo))
            
            # 4. Se foi um comando de aprendizado, salva na memória
            if "aprender" in user_input.lower():
                nome_comando = user_input.split(" ")[1] # Ex: "aprender limpar ..."
                save_memory(nome_comando, codigo)
    else:
        print(f"Soia: {resposta}")