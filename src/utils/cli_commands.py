import sys
import os
from rich import box
from rich.console import Console
from rich.panel import Panel

sys.path.append(os.path.join(os.path.dirname(__file__)))

from project_builder import frontend_react, frontend_nextjs, frontend_typescript, frontend_base

console = Console()

def help_flags_cli():
  
  flags = '''
  --path [bold]Takes a origin path[/bold]
  --type [bold]Type of project[/bold]
  --tech [bold]Technology of project[/bold]
  --reset [bold]Reset your config (JSON)[/bold]
  '''
  
  
  console.print(Panel(
    flags,
    style="dim white",
    title="Flags Commands",
    title_align="left",
    border_style="bold green",
  ))
  

def create_cli(type: str, tech: str, path: str):
  match type:
    case "frontend":
      
      match tech:
        case "default":
          frontend_base(path)
        case "react":
          frontend_react(path)
        case "nextjs":
          frontend_nextjs(path)
        case "typescript":
          frontend_typescript(path)
          
    case "backend":
      print("Function in development")
    case "fullstack":
      print("Function in development")
      