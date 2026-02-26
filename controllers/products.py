from flask import Blueprint, render_template, redirect, request, url_for
from repositories.product_repository import ProductRepository
from models.product import Product
from repositories.category_repository import CategoryRepository
from datetime import datetime

products_bp = Blueprint("products", __name__)

category_repository = CategoryRepository()
product_repository = ProductRepository()


@products_bp.route("/products")
def getAll():
    data = product_repository.getAll()
    return render_template("products/products.html", products=data)


@products_bp.route("/new_product", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        category = request.form.get("category")

        product = Product(
            0, datetime.now(), None, name, description, quantity, price, category
        )

        product_repository.create(product)

        return redirect(url_for("products.products"))

    categories = category_repository.getAll()
    return render_template("products/new_product.html", categories=categories)


@products_bp.route("/update_product", methods=["GET", "POST"])
def update():
    return True
