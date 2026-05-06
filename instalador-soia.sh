#!/usr/bin/env bash

set -euo pipefail

REPO_URL="https://github.com/ArthurEnzol/Soia-Alpha.git"
PROJECT_DIR="$HOME/Soia-Alpha"
VENV_DIR="$PROJECT_DIR/.venv"
BIN_DIR="$HOME/.local/bin"
SOIA_BIN="$BIN_DIR/soia"
REQ_FILE="$PROJECT_DIR/requirements.txt"
REQ_STAMP="$VENV_DIR/.requirements.sha256"
REMOTE_NAME="origin"
REMOTE_BRANCH="main"

require_command() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Erro: comando obrigatorio nao encontrado: $1"
        exit 1
    fi
}

file_hash() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "$1" | awk '{print $1}'
    else
        cksum "$1" | awk '{print $1 "-" $2}'
    fi
}

ensure_pip() {
    if ! "$VENV_DIR/bin/python" -m pip --version >/dev/null 2>&1; then
        "$VENV_DIR/bin/python" -m ensurepip --upgrade
    fi
}

install_requirements_if_needed() {
    if [ ! -f "$REQ_FILE" ]; then
        echo "Aviso: requirements.txt nao encontrado em $PROJECT_DIR."
        return
    fi

    current_requirements_hash="$(file_hash "$REQ_FILE")"
    installed_requirements_hash=""

    if [ -f "$REQ_STAMP" ]; then
        installed_requirements_hash="$(cat "$REQ_STAMP")"
    fi

    if [ "$current_requirements_hash" != "$installed_requirements_hash" ]; then
        echo "Instalando dependencias no venv..."
        ensure_pip
        "$VENV_DIR/bin/python" -m pip install --upgrade pip
        "$VENV_DIR/bin/python" -m pip install -r "$REQ_FILE"
        echo "$current_requirements_hash" > "$REQ_STAMP"
    else
        echo "Dependencias ja instaladas para este requirements.txt."
    fi
}

echo "Instalando SOIA..."

require_command git
require_command python3

mkdir -p "$BIN_DIR"

if [ -d "$PROJECT_DIR/.git" ]; then
    echo "Repositorio encontrado em $PROJECT_DIR"
    if git -C "$PROJECT_DIR" remote get-url "$REMOTE_NAME" >/dev/null 2>&1; then
        git -C "$PROJECT_DIR" remote set-url "$REMOTE_NAME" "$REPO_URL"
    else
        git -C "$PROJECT_DIR" remote add "$REMOTE_NAME" "$REPO_URL"
    fi
    echo "Atualizando repositorio..."
    git -C "$PROJECT_DIR" pull --ff-only "$REMOTE_NAME" "$REMOTE_BRANCH"
elif [ -e "$PROJECT_DIR" ]; then
    echo "Erro: $PROJECT_DIR ja existe, mas nao e um repositorio git."
    echo "Remova ou renomeie essa pasta antes de instalar."
    exit 1
else
    echo "Clonando repositorio em $PROJECT_DIR..."
    git clone "$REPO_URL" "$PROJECT_DIR"
fi

if [ ! -x "$VENV_DIR/bin/python" ]; then
    echo "Criando ambiente virtual em $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Ambiente virtual ja existe."
fi

install_requirements_if_needed

echo "Criando comando global: soia"

cat > "$SOIA_BIN" << EOF
#!/usr/bin/env bash

set -e

PROJECT_DIR="\$HOME/Soia-Alpha"
VENV_DIR="\$PROJECT_DIR/.venv"
MAIN_SCRIPT="\$PROJECT_DIR/main.py"
REQ_FILE="\$PROJECT_DIR/requirements.txt"
REQ_STAMP="\$VENV_DIR/.requirements.sha256"
REPO_URL="https://github.com/ArthurEnzol/Soia-Alpha.git"
REMOTE_NAME="origin"
REMOTE_BRANCH="main"

file_hash() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "\$1" | awk '{print \$1}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "\$1" | awk '{print \$1}'
    else
        cksum "\$1" | awk '{print \$1 "-" \$2}'
    fi
}

ensure_pip() {
    if ! "\$VENV_DIR/bin/python" -m pip --version >/dev/null 2>&1; then
        "\$VENV_DIR/bin/python" -m ensurepip --upgrade
    fi
}

install_requirements_if_needed() {
    if [ ! -f "\$REQ_FILE" ]; then
        return
    fi

    current_requirements_hash="\$(file_hash "\$REQ_FILE")"
    installed_requirements_hash=""

    if [ -f "\$REQ_STAMP" ]; then
        installed_requirements_hash="\$(cat "\$REQ_STAMP")"
    fi

    if [ "\$current_requirements_hash" != "\$installed_requirements_hash" ]; then
        echo "Atualizando dependencias..."
        ensure_pip
        "\$VENV_DIR/bin/python" -m pip install -r "\$REQ_FILE"
        echo "\$current_requirements_hash" > "\$REQ_STAMP"
    fi
}

ensure_remote() {
    if git remote get-url "\$REMOTE_NAME" >/dev/null 2>&1; then
        git remote set-url "\$REMOTE_NAME" "\$REPO_URL"
    else
        git remote add "\$REMOTE_NAME" "\$REPO_URL"
    fi
}

ask_for_update() {
    if ! command -v git >/dev/null 2>&1; then
        return
    fi

    if [ ! -d "\$PROJECT_DIR/.git" ]; then
        return
    fi

    cd "\$PROJECT_DIR"
    ensure_remote

    if ! git fetch --quiet "\$REMOTE_NAME" "\$REMOTE_BRANCH"; then
        echo "Aviso: nao foi possivel verificar atualizacoes."
        return
    fi

    local_commit="\$(git rev-parse HEAD)"
    remote_commit="\$(git rev-parse "\$REMOTE_NAME/\$REMOTE_BRANCH")"

    if [ "\$local_commit" = "\$remote_commit" ]; then
        return
    fi

    if ! git diff --quiet || ! git diff --cached --quiet; then
        echo "Existe uma atualizacao, mas ha alteracoes locais. Atualizacao ignorada."
        return
    fi

    echo "Existe uma nova versao da SOIA disponivel."
    read -r -p "Deseja atualizar agora? [s/N]: " resposta

    case "\$resposta" in
        s|S|sim|SIM|Sim)
            git pull --ff-only "\$REMOTE_NAME" "\$REMOTE_BRANCH"
            install_requirements_if_needed
            ;;
        *)
            echo "Atualizacao ignorada."
            ;;
    esac
}

if [ ! -x "\$VENV_DIR/bin/python" ]; then
    echo "Erro: venv nao encontrado em \$VENV_DIR."
    echo "Rode o instalador novamente."
    exit 1
fi

if [ ! -f "\$MAIN_SCRIPT" ]; then
    echo "Erro: main.py nao encontrado em \$MAIN_SCRIPT."
    exit 1
fi

cd "\$PROJECT_DIR"
ask_for_update
source "\$VENV_DIR/bin/activate"
python "\$MAIN_SCRIPT" "\$@"
EOF

chmod +x "$SOIA_BIN"

echo ""
echo "Instalacao concluida."
echo "Projeto: $PROJECT_DIR"
echo "Comando: $SOIA_BIN"

if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo ""
    echo "Aviso: $BIN_DIR nao esta no PATH."
    echo "Adicione esta linha ao seu ~/.bashrc, ~/.zshrc ou equivalente:"
    echo "export PATH=\"\$HOME/.local/bin:\$PATH\""
fi

echo ""
echo "Use: soia"
