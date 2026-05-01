import os

def executar():
    try:
        target_dir = input("Digite o caminho do diretório onde deseja criar o projeto (ex: ~/projects/react): ").strip()
        if not target_dir:
            target_dir = os.path.expanduser("~")

        project_path = os.path.join(target_dir, "react-project")
        os.makedirs(project_path, exist_ok=True)

        public_dir = os.path.join(project_path, "public")
        src_dir = os.path.join(project_path, "src")
        os.makedirs(public_dir, exist_ok=True)
        os.makedirs(src_dir, exist_ok=True)

        print(f"Estrutura do projeto React criada em: {project_path}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    executar()