from services.product_service import ProductService
from services.category_service import CategoryService

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from flask import Flask, render_template

from tui import TUI

app = Flask(__name__)

category_service = CategoryService()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/categories")
def categories():
    data = category_service.getAll()
    return render_template("categories.html", categories=data)


@app.route("/products")
def products():
    return "products.html"


@app.route("/cash")
def cash():
    return "cash.html"


if __name__ == "__main__":
    app.run(debug=True)

# console = Console()

# console.print(
#     Panel(
#         "PyStorage - Welcome!",
#         style="white on blue",
#         expand=True,
#     )
# )


# def menu():
#     global app
#     options = [
#         "Product - GetAll",
#         "Product - Create",
#         "Product - Get",
#         "Product - Delete",
#     ]

#     menu_text = "\n".join(
#         [f"[bold cyan]{i+1}[/bold cyan]. {opt}" for i, opt in enumerate(options)]
#     )
#     console.print(Panel(menu_text, title="Main menu", expand=False))

#     choice = Prompt.ask(
#         "Choose an option", choices=["1", "2", "3", "4", "5"], default="1"
#     )
#     print(choice)

#     if choice == 1:
#         TUI.printCategoriesList()
#     elif choice == 2:
#         TUI.createProductInput()
#     elif choice == 3:
#         TUI.getProduct()
#     elif choice == 4:
#         TUI.deleteProduct()
#     else:
#         return


# menu()


# TUI.printCategoriesList()
# TUI.createCategoryInput()
# TUI.printCategoriesList()

# TUI.getProduct()
# TUI.getProductsTotal()
# TUI.deleteProduct()
