"""
Constantes para geração de projetos frontend.
Organizadas por categoria: Base, NextJS, TypeScript, React.
"""

# =============================================================================
# UI / BRANDING
# =============================================================================

SOIA_LOGO = """
  ██╗ ██╗    ███████╗ ██████╗ ██╗ █████╗     ██╗ ██╗  
 ██╔╝██╔╝    ██╔════╝██╔═══██╗██║██╔══██╗    ╚██╗╚██╗ 
██╔╝██╔╝     ███████╗██║   ██║██║███████║     ╚██╗╚██╗
╚██╗╚██╗     ╚════██║██║   ██║██║██╔══██║     ██╔╝██╔╝
 ╚██╗╚██╗    ███████║╚██████╔╝██║██║  ██║    ██╔╝██╔╝ 
  ╚═╝ ╚═╝    ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═╝ ╚═╝  
"""


# =============================================================================
# BASE TEMPLATES (HTML/CSS/JS)
# =============================================================================

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto Front-End</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Projeto Criado com Sucesso!</h1>
    <script src="js/script.js"></script>
</body>
</html>"""

CSS_TEMPLATE = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
}"""

JS_TEMPLATE = "console.log('Script carregado com sucesso!');"


# =============================================================================
# NEXTJS TEMPLATES
# =============================================================================

NEXT_PACKAGE_JSON = """{
  "name": "nextjs-executor-projeto",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  },
  "devDependencies": {
    "typescript": "latest",
    "@types/node": "latest",
    "@types/react": "latest",
    "@types/react-dom": "latest"
  }
}"""

NEXT_LAYOUT = """export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-br">
      <head>
        <style>{`
          body { 
            margin: 0; 
            font-family: sans-serif; 
            background: #0f172a; 
            color: #f8fafc;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
          }
        `}</style>
      </head>
      <body>{children}</body>
    </html>
  )
}"""

NEXT_PAGE = """export default function Page() {
  return (
    <div style={{ textAlign: 'center' }}>
      <h1 style={{ color: '#22c55e' }}> Next.js Executável!</h1>
      <p>Projeto gerado com sucesso pelo seu Python Builder.</p>
      <code style={{ background: '#1e293b', padding: '5px', borderRadius: '5px' }}>
        src/app/page.tsx
      </code>
    </div>
  )
}"""

NEXT_CONFIG = """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}
module.exports = nextConfig"""

NEXT_GLOBALS_CSS = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #0f172a;
  color: #f8fafc;
  font-family: system-ui, -apple-system, sans-serif;
}"""

NEXT_TS_CONFIG = """{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}"""

TAILWIND_CONFIG = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}"""


# =============================================================================
# TYPESCRIPT + VITE TEMPLATES
# =============================================================================

TS_PACKAGE_JSON = """{
  "name": "react-ts-project",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.0.0",
    "typescript": "^5.0.0",
    "vite": "^4.0.0"
  }
}"""

TS_VITE_CONFIG = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})"""

TS_INDEX_HTML = """<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>"""

TS_MAIN = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)"""

TS_APP = """import React from 'react';

function App() {
  return (
    <div style={{ backgroundColor: '#242424', color: 'white', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <h1>React + TypeScript Criado!</h1>
    </div>
  );
}

export default App;"""


# =============================================================================
# REACT + VITE TEMPLATES
# =============================================================================

REACT_PACKAGE_JSON = """{
  "name": "react-project",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.0",
    "vite": "^4.0.0"
  }
}"""

REACT_VITE_CONFIG = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})"""

REACT_INDEX_HTML = """<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React + Vite</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>"""

REACT_MAIN = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)"""

REACT_APP = """function App() {
  return (
    <div className="container">
      <h1>React + Vite Criado! ⚛️</h1>
      <p>Edite o arquivo src/App.jsx para começar.</p>
    </div>
  )
}

export default App"""

REACT_INDEX_CSS = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #0f172a;
  color: #f8fafc;
  font-family: system-ui, -apple-system, sans-serif;
}"""

