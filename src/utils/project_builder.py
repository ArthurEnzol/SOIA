import os
from pathlib import Path
from src.core.constants import (
    HTML_TEMPLATE, CSS_TEMPLATE, JS_TEMPLATE,
    NEXT_LAYOUT, NEXT_PAGE, NEXT_CONFIG, NEXT_GLOBALS_CSS, NEXT_PACKAGE_JSON, NEXT_TS_CONFIG, TAILWIND_CONFIG,
    TS_APP, TS_INDEX_HTML, TS_MAIN, TS_PACKAGE_JSON, TS_VITE_CONFIG,
    REACT_APP, REACT_MAIN, REACT_PACKAGE_JSON, REACT_VITE_CONFIG, REACT_INDEX_HTML, REACT_INDEX_CSS
)

"""Cria a estrutura base do frontend"""
def frontend_base(path: str):
  base = Path(path)

  '''
    Create a base structure from a basic frontend project
  '''
  
  """Cria as pastas"""
  (base / "css").mkdir(parents=True, exist_ok=True)
  (base / "js").mkdir(parents=True, exist_ok=True)
  (base / "assets").mkdir(parents=True, exist_ok=True)
  (base / "imgs").mkdir(parents=True, exist_ok=True)
  
  """Cria os arquivos"""
  (base / "index.html").write_text(HTML_TEMPLATE)
  (base / "css/style.css").write_text(CSS_TEMPLATE)
  (base / "js/script.js").write_text(JS_TEMPLATE)

def frontend_react(path: str):

    """
        Create a frontend project structure with react
    """

    base = Path(path)
    
    folders = [
        "public",
        "src/assets",
        "src/components",
        "src/hooks",
        "src/context",
        "src/services"
    ]
    
    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)
        
    # --- Arquivos na Raiz ---
    (base / "package.json").write_text(REACT_PACKAGE_JSON, encoding="utf-8")
    (base / "vite.config.js").write_text(REACT_VITE_CONFIG, encoding="utf-8")
    (base / "index.html").write_text(REACT_INDEX_HTML, encoding="utf-8")
    (base / ".gitignore").write_text("node_modules\ndist\n.env", encoding="utf-8")

    # --- Arquivos no SRC ---
    (base / "src/main.jsx").write_text(REACT_MAIN, encoding="utf-8")
    (base / "src/App.jsx").write_text(REACT_APP, encoding="utf-8")
    (base / "src/index.css").write_text(REACT_INDEX_CSS, encoding="utf-8")

def frontend_typescript(path: str):

    """
        Create a frontend project structure with typescript
    """
    
    base = Path(path)
    
    folders = [
        "public",
        "src/assets",
        "src/components",
        "src/hooks",
        "src/pages",
        "src/types",   
        "src/utils"    
    ]
    
    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)
    
    '''Arquivos da Raiz'''
    (base / "package.json").write_text(TS_PACKAGE_JSON, encoding="utf-8")
    (base / "vite.config.ts").write_text(TS_VITE_CONFIG, encoding="utf-8")
    (base / "index.html").write_text(TS_INDEX_HTML, encoding="utf-8")
    (base / "tsconfig.json").write_text(NEXT_TS_CONFIG, encoding="utf-8") 
    
    '''Arquivos do SRC'''
    (base / "src/main.tsx").write_text(TS_MAIN, encoding="utf-8")
    (base / "src/App.tsx").write_text(TS_APP, encoding="utf-8")
    (base / "src/types/index.ts").write_text("// Defina seus types aqui",encoding="utf-8")
    
    
def frontend_nextjs(path: str):
    base = Path(path)

    """
        Create a frontend project structure with nextJS
    """
    
    folders = [
        "public/assets",
        "src/app",           
        "src/app/api",      
        "src/components",
        "src/lib",           
        "src/styles"
    ]
    
    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)
        
    '''Arquivos obrigatórios do Next.js 13+'''
    (base / "src/app/layout.tsx").write_text(NEXT_LAYOUT) 
    (base / "src/app/page.tsx").write_text(NEXT_PAGE)
    (base / "src/app/globals.css").write_text(NEXT_GLOBALS_CSS)
    (base / "package.json").write_text(NEXT_PACKAGE_JSON)
    (base / "next.config.js").write_text(NEXT_CONFIG)
    (base / "tailwind.config.js").write_text(TAILWIND_CONFIG, encoding="utf-8")

