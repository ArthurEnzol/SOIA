"""Painel ao vivo com informações do sistema (atualização periódica)."""
from __future__ import annotations

import os
import platform
import socket
import sys
import threading
import time
from datetime import datetime

import psutil
from rich import box
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

REFRESH_SEC = 0.5


def _bar(pct: float, width: int = 24) -> Text:
    pct = max(0.0, min(100.0, pct))
    n = int(round(width * pct / 100.0))
    if pct < 60:
        fill_style = "bold green"
    elif pct < 85:
        fill_style = "bold yellow"
    else:
        fill_style = "bold red"
    bar = "█" * n + "░" * (width - n)
    t = Text()
    t.append(bar[:n], style=fill_style)
    if n < width:
        t.append(bar[n:], style="dim")
    t.append(f"  {pct:5.1f}%", style="bold white")
    return t


def _fmt_bytes(n: int) -> str:
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if abs(n) < 1024.0:
            return f"{n:.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PiB"


def _build_dashboard(console: Console) -> Panel:
    uname = platform.uname()
    vm = psutil.virtual_memory()
    sw = psutil.swap_memory()
    cpu_pct = psutil.cpu_percent(interval=None)
    load_txt = "—"
    try:
        load = os.getloadavg()  # type: ignore[attr-defined]
        load_txt = f"{load[0]:.2f}  {load[1]:.2f}  {load[2]:.2f}"
    except (AttributeError, OSError):
        pass

    boot = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M")

    meta = Table.grid(padding=(0, 2))
    meta.add_column(style="cyan bold", justify="right")
    meta.add_column(style="white")

    meta.add_row("SO / kernel", f"{uname.system} {uname.release}")
    meta.add_row("Hostname", socket.gethostname())
    meta.add_row("Arquitetura", uname.machine)
    meta.add_row("Processador", (platform.processor() or "—")[:64])
    meta.add_row("Python", sys.version.split()[0])
    meta.add_row("PID atual", str(os.getpid()))
    meta.add_row("Boot", boot)
    meta.add_row("Load avg", load_txt)

    bars = Table.grid(padding=(0, 1))
    bars.add_column("Recurso", style="bold dim")
    bars.add_column(Text())
    bars.add_row("CPU ", _bar(cpu_pct))
    bars.add_row("RAM ", _bar(vm.percent))
    bars.add_row("Swap", _bar(sw.percent))

    ram_line = f"{_fmt_bytes(vm.used)} / {_fmt_bytes(vm.total)}  ·  livre {_fmt_bytes(vm.available)}"
    bars.add_row("", Text(ram_line, style="dim"))

    disk_tbl = Table(
        box=box.SIMPLE_HEAD,
        border_style="dim blue",
        title="Discos",
        expand=False,
    )
    disk_tbl.add_column("Montagem", style="cyan", no_wrap=True)
    disk_tbl.add_column("Uso", justify="right")
    disk_tbl.add_column("Livre", justify="right")
    disk_tbl.add_column("Barra", overflow="ellipsis")

    for part in psutil.disk_partitions(all=False):
        try:
            u = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue
        disk_tbl.add_row(
            part.mountpoint[:28],
            f"{u.percent:.0f}%",
            _fmt_bytes(u.free),
            _bar(float(u.percent), width=14),
        )

    try:
        net = psutil.net_io_counters()
        net_line = (
            f"enviado {_fmt_bytes(net.bytes_sent)}  ·  "
            f"recebido {_fmt_bytes(net.bytes_recv)}"
        )
    except Exception:
        net_line = "—"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = Text.from_markup(
        f"[bold green]SOIA[/] · sistema ao vivo  [dim]{now}[/]  [yellow]⟳[/] [dim]{REFRESH_SEC}s[/]"
    )

    body = Group(
        header,
        Text(""),
        meta,
        Text(""),
        bars,
        Text(""),
        disk_tbl,
        Text(""),
        Text(f"Rede (total desde boot): {net_line}", style="dim"),
    )

    term_w = console.width
    panel_w = None
    if term_w and term_w > 0:
        panel_w = max(52, min(term_w - 2, 92))

    return Panel(
        body,
        title="[bold]Informações do sistema[/]",
        subtitle="Pressione [bold]Enter[/] para sair",
        border_style="bright_blue",
        box=box.DOUBLE_EDGE,
        padding=(1, 2),
        width=panel_w,
    )


def run_infosystem_live() -> None:
    """Atualiza o painel a cada ~0,5 s até Enter."""
    console = Console()
    stop = threading.Event()

    # Primeira leitura de CPU (psutil)
    psutil.cpu_percent(interval=0.1)

    def wait_enter() -> None:
        try:
            input()
        except (EOFError, KeyboardInterrupt):
            pass
        stop.set()

    threading.Thread(target=wait_enter, daemon=True).start()

    try:
        with Live(
            _build_dashboard(console),
            console=console,
            refresh_per_second=1 / REFRESH_SEC,
            transient=False,
        ) as live:
            while not stop.is_set():
                live.update(_build_dashboard(console))
                time.sleep(REFRESH_SEC)
    finally:
        console.print()
