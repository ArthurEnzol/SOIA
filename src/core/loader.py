import os
import time
import random
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

console = Console()

def load_project(directory):
    """Exibe animação de carregamento do projeto."""
    console.print("\n[bold green]── ANALISANDO ESTRUTURA DE DADOS ──[/bold green]", justify="center")
    
    itens = [os.path.join(directory, item) for item in os.listdir(directory)]
    total = len(itens)
    
    tabela = Table(show_header=True, header_style="bold cyan", box=None)
    tabela.add_column("ID", style="dim", width=12)
    tabela.add_column("ARQUIVO", style="bold green")
    tabela.add_column("STATUS", justify="right")

    with Live(tabela, refresh_per_second=10) as live:
        for i, nome in enumerate(itens):
            porcentagem = int((i + 1) / total * 100)
            file_id = hex(random.randint(0x1000, 0xffff))
            status = "[bold green]OK[/bold green]" if random.random() > 0.1 else "[bold yellow]BYPASS[/bold yellow]"
            
            tabela.add_row(f"{file_id}", f"{nome[:25]}", status)
            console.print(f"[bold green] STATUS DA SOIA: {porcentagem}% COMPLETO [/bold green]", end="\r")
            time.sleep(random.uniform(0.02, 0.1))

    console.print("\n" + "═" * 50, style="green")
    msg_final = Panel.fit(
        f"[bold white]ACESSO CONCEDIDO[/bold white]\n[green]{total} ARQUIVOS SINCRONIZADOS NA MEMÓRIA DA SOIA[/green]",
        border_style="bold green",
        title="[SYSTEM ONLINE]"
    )
    console.print(msg_final, justify="center")
