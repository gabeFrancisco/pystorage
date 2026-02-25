from flask import Blueprint, render_template, request

home_bp = Blueprint("/", __name__)


@home_bp.route("/")
def index():
    return render_template("index.html")
