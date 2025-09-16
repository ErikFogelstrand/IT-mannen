from flask import Blueprint, render_template
from database.pr import *


_view = Blueprint("view", __name__, template_folder="templates")


@_view.route("/view/<id>", methods=["GET"])
def view(id: str) -> str:
    id = int(id)
    posts = get_content_from_postview(id)
    return render_template("view.html", posts=posts)


def create_blueprint() -> Blueprint:
    return _view
