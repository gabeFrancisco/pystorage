from services.product_service import ProductService
from services.category_service import CategoryService

from flask import Flask, render_template, redirect, url_for, request, abort
from models.category import Category
from datetime import datetime

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


@app.route("/new_category", methods=["GET", "POST"])
def new_category():

    if request.method == "POST":
        name = request.form.get("name")

        if name is None or name == "":
            abort(400, "The name field is required!")

        category = Category(id=0, created_at=datetime.now(), updated_at=None, name=name)
        category_service.create(category)

        return redirect(url_for("categories"))

    return render_template("new_category.html")


@app.route("/update_category/<int:category_id>", methods=["GET", "POST"])
def update_category(category_id):
    dbCategory = category_service.get(category_id)

    if request.method == "POST":
        name = request.form.get("name")

        if name is None or name == "":
            abort(400, "The name field is required!")

        dbCategory.name = name
        category_service.update(dbCategory)

        return redirect(url_for("categories"))

    return render_template("update_category.html", category=dbCategory)


@app.route("/delete_category/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    if category_id is None or category_id == 0:
        abort(400, "Invalid ID!")

    category_service.delete(category_id)


@app.route("/products")
def products():
    return "products.html"


if __name__ == "__main__":
    app.run(debug=True)
