#!/bin/bash
# =============================================
# INSTALADOR UNIVERSAL - SOIA
# Funciona na maioria das distros Linux
# =============================================

set -e  # Para em caso de erro

echo "🚀 Iniciando Instalação do Soia..."
echo "==================================="

# ===================== VARIÁVEIS =====================
REPO_URL="https://github.com/ArthurEnzol/Soia-Alpha.git"
INSTALL_DIR="$HOME/SOIA"
DEFAULT_PROJECT="$INSTALL_DIR/Soia-Alpha"

# ===================== DETECÇÃO DO SHELL =====================
CURRENT_SHELL=$(basename "$SHELL")

echo "🔍 Shell detectado: $CURRENT_SHELL"

# ===================== CRIAÇÃO DA PASTA E CLONE =====================
echo "📂 Criando pasta $INSTALL_DIR..."

mkdir -p "$INSTALL_DIR"

if [ -d "$DEFAULT_PROJECT" ]; then
    echo "⚠️  Projeto já existe. Atualizando..."
    cd "$DEFAULT_PROJECT" && git pull
else
    echo "⬇️  Clonando repositório..."
    git clone "$REPO_URL" "$DEFAULT_PROJECT"
fi

# ===================== CONFIGURAÇÃO DO SHELL =====================
echo "⚙️  Configurando atalho 'soia'..."

case "$CURRENT_SHELL" in
    fish)
        CONFIG_FILE="$HOME/.config/fish/config.fish"
        mkdir -p "$HOME/.config/fish"
        
        # Adiciona função no Fish
        cat >> "$CONFIG_FILE" << 'EOF'

# =============================================
# SOIA - Atalho automático
# =============================================
function soia
    set -l project_dir ""
    
    if test (count $argv) -gt 0; and test -d $argv[1]
        set project_dir $argv[1]
        set -e argv[1]
    else
        set project_dir "$HOME/SOIA/Soia-Alpha"
    end

    set -l venv_python "$project_dir/.venv/bin/python3"
    set -l main_script "$project_dir/main.py"

    if not test -f "$main_script"
        echo "❌ Erro: main.py não encontrado em $project_dir"
        return 1
    end

    if not test -f "$venv_python"
        echo "❌ Erro: Ambiente virtual não encontrado. Rode: python -m venv .venv"
        return 1
    end

    echo "🚀 Soia → $project_dir"
    $venv_python $main_script $argv
end
EOF
        echo "✅ Função adicionada ao Fish Shell"
        ;;

    bash)
        CONFIG_FILE="$HOME/.bashrc"
        cat >> "$CONFIG_FILE" << 'EOF'

# =============================================
# SOIA - Atalho automático
# =============================================
soia() {
    local project_dir="${1:-$HOME/SOIA/Soia-Alpha}"
    local venv_python="$project_dir/.venv/bin/python3"
    local main_script="$project_dir/main.py"

    if [ ! -f "$main_script" ]; then
        echo "❌ Erro: main.py não encontrado em $project_dir"
        return 1
    fi

    if [ ! -f "$venv_python" ]; then
        echo "❌ Erro: Ambiente virtual não encontrado"
        return 1
    fi

    echo "🚀 Soia → $project_dir"
    $venv_python "$main_script" "${@:2}"
}
EOF
        echo "✅ Função adicionada ao Bash"
        ;;

    zsh)
        CONFIG_FILE="$HOME/.zshrc"
        # Similar ao bash (pode adicionar depois se precisar)
        echo "⚠️  Zsh detectado - função básica adicionada"
        ;;
        
    *)
        echo "⚠️  Shell não suportado automaticamente: $CURRENT_SHELL"
        echo "   Adicione manualmente a função."
        ;;
esac

# ===================== FINALIZAÇÃO =====================
echo ""
echo "🎉 Instalação concluída com sucesso!"
echo ""
echo "📁 Local do projeto: $DEFAULT_PROJECT"
echo "🔧 Comando disponível: soia"
echo ""
echo "Para usar:"
echo "   soia                    → Executa o projeto padrão"
echo "   soia /outro/projeto     → Executa em outro diretório"
echo ""
echo "Recarregue seu shell:"
if [ "$CURRENT_SHELL" = "fish" ]; then
    echo "   source ~/.config/fish/config.fish"
else
    echo "   source $CONFIG_FILE"
fi

echo ""
echo "Deseja testar agora? (s/N)"
read -r test_now
if [[ "$test_now" =~ ^[Ss]$ ]]; then
    echo "Testando..."
    soia
fi