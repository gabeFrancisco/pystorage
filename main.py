from repositories.product_repository import ProductRepository
from repositories.category_repository import CategoryRepository

from flask import Flask, render_template, redirect, url_for, request, abort
from models.category import Category
from models.product import Product
from datetime import datetime

app = Flask(__name__)

category_repository = CategoryRepository()
product_repository = ProductRepository()

from controllers.home import home_bp

app.register_blueprint(home_bp)

# CATEGORIAS ------------------------------------------------------------------------------


@app.route("/categories")
def categories():
    data = category_repository.getAll()
    return render_template("categories/categories.html", categories=data)


@app.route("/new_category", methods=["GET", "POST"])
def new_category():

    if request.method == "POST":
        name = request.form.get("name")

        if name is None or name == "":
            abort(400, "The name field is required!")

        category = Category(id=0, created_at=datetime.now(), updated_at=None, name=name)
        category_repository.create(category)

        return redirect(url_for("categories"))

    return render_template("categories/new_category.html")


@app.route("/update_category/<int:category_id>", methods=["GET", "POST"])
def update_category(category_id):
    dbCategory = category_repository.get(category_id)

    if request.method == "POST":
        name = request.form.get("name")

        if name is None or name == "":
            abort(400, "The name field is required!")

        dbCategory.name = name
        category_repository.update(dbCategory)

        return redirect(url_for("categories"))

    return render_template("categories/update_category.html", category=dbCategory)


@app.route("/delete_category/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    if category_id is None or category_id == 0:
        abort(400, "Invalid ID!")

    category_repository.delete(category_id)


# PRODUTOS ------------------------------------------------------------------------------


@app.route("/products")
def products():
    data = product_repository.getAll()
    return render_template("products/products.html", products=data)


@app.route("/new_product", methods=["GET", "POST"])
def new_product():
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

        return redirect(url_for("products"))

    categories = category_repository.getAll()
    return render_template("products/new_product.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
