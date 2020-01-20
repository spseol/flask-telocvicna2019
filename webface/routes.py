from . import app
from .models import Uzivatel
from flask import render_template, request, redirect, url_for
from pony.orm import db_session
from werkzeug.security import check_password_hash


@app.route("/", methods=["GET"])
def index():
    return render_template("base.html.j2")


@app.route("/", methods=["POST"])
def index_post():
    login = request.form.get("login")
    heslo = request.form.get("heslo")
    print(login)
    if login and heslo:
        with db_session:
            uzivatel = Uzivatel.get(login=login)
            if uzivatel:
                pwhash = uzivatel.heslo
            else:
                pwhash = None
        check_password_hash(pwhash, heslo)
    return redirect(url_for("index"))
