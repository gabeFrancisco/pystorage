from flask import Blueprint, render_template, request
from repositories.info_repository import InfoRepository

home_bp = Blueprint("home", __name__)

infoRepository = InfoRepository()


@home_bp.route("/")
def index():
    dbSize = infoRepository.getDbSize()
    return render_template("index.html", dbSize=dbSize)
