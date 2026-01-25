from services.product_service import ProductService

from rich.console import Console
from rich.panel import Panel

from tui import TUI

console = Console()

console.print(
    Panel(
        "PyStorage - Welcome!",
        style="white on blue",
        expand=True,
    )
)

TUI.printProductsList()
# TUI.createProductInput()
TUI.getProduct()
