# Soia

Sistema inteligente de automação e assistência pessoal.

---

## Sobre o Projeto

**Soia** é um assistente pessoal desenvolvido em Python que visa automatizar tarefas, organizar informações e auxiliar o usuário em suas atividades diárias.

---

## Instalação Rápida (Recomendado)

A forma mais simples de instalar o Soia é utilizando o instalador automático.

### 1. Baixar o instalador

```bash
curl -O https://raw.githubusercontent.com/ArthurEnzol/Soia-Alpha/main/instalar-soia.sh
Ou, se preferir usar wget:
Bashwget https://raw.githubusercontent.com/ArthurEnzol/Soia-Alpha/main/instalar-soia.sh
2. Executar o instalador
Bashchmod +x instalar-soia.sh
./instalar-soia.sh
O instalador irá:

Criar a pasta ~/SOIA em seu diretório pessoal
Clonar o repositório do projeto
Configurar o comando soia no seu shell (Fish, Bash ou Zsh)
Deixar tudo pronto para uso


Como Usar
Após a instalação, você pode executar o Soia de qualquer diretório:
Bashsoia
Usando em outro diretório
Bashsoia /caminho/para/outro/projeto
Passando argumentos
Bashsoia --modo debug
soia --ajuda

Atualização
Para atualizar o Soia no futuro, basta executar novamente o instalador:
Bash./instalar-soia.sh
Ou navegar até a pasta do projeto e puxar as atualizações:
Bashcd ~/SOIA/Soia-Alpha
git pull

Requisitos

Git
Python 3.10 ou superior
Virtual Environment (venv)
Shell compatível (Fish, Bash ou Zsh)


Estrutura de Pastas
text~/SOIA/
└── Soia-Alpha/          # Código principal do projeto
    ├── main.py
    ├── .venv/           # Ambiente virtual
    ├── config.json
    └── ...

Suporte
Caso tenha algum problema durante a instalação, sinta-se à vontade para abrir uma Issue no repositório.

Desenvolvido por Arthur Enzol
text---

Este README é limpo, profissional, bem organizado e direto. Ele foca exatamente no que você pediu: explicar o que é o Soia e orientar o usuário a baixar **apenas o instalador**.

Quer que eu ajuste algum texto, adicione seções ou mude o tom?