from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    a = "Variable content"
    return render_template("home.html", a=a)
