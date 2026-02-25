from repositories.category_repository import CategoryRepository

from flask import Flask, render_template, redirect, url_for, request, abort
from models.category import Category

from datetime import datetime

app = Flask(__name__)


from controllers.home import home_bp
from controllers.products import products_bp
from controllers.categories import categories_bp

app.register_blueprint(home_bp)
app.register_blueprint(products_bp)
app.register_blueprint(categories_bp)

if __name__ == "__main__":
    app.run(debug=True)
