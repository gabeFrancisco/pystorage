from flask import Blueprint, url_for, render_template, request, abort, redirect
from datetime import datetime
from models.category import Category
from repositories.category_repository import CategoryRepository

categories_bp = Blueprint("categories", __name__)

category_repository = CategoryRepository()


@categories_bp.route("/categories")
def getAll():
    data = category_repository.getAll()
    return render_template("categories/categories.html", categories=data)


@categories_bp.route("/new_category", methods=["GET", "POST"])
def new():

    if request.method == "POST":
        name = request.form.get("name")

        if name is None or name == "":
            abort(400, "The name field is required!")

        category = Category(id=0, created_at=datetime.now(), updated_at=None, name=name)
        category_repository.create(category)

        return redirect(url_for("categories.categories"))

    return render_template("categories/new_category.html")


@categories_bp.route("/update_category/<int:category_id>", methods=["GET", "POST"])
def update(category_id):
    dbCategory = category_repository.get(category_id)

    if request.method == "POST":
        name = request.form.get("name")

        if name is None or name == "":
            abort(400, "The name field is required!")

        dbCategory.name = name
        category_repository.update(dbCategory)

        return redirect(url_for("categories.categories"))

    return render_template("categories/update_category.html", category=dbCategory)


@categories_bp.route("/delete_category/<int:category_id>", methods=["DELETE"])
def delete(category_id):
    if category_id is None or category_id == 0:
        abort(400, "Invalid ID!")

    category_repository.delete(category_id)
