from . import app
from .models import Uzivatel
from flask import render_template, request
from pony.orm import db_session
from werkzeug.security import check_password_hash


@app.route('/')
def index():
    login = request.form.get('login')
    heslo = request.form.get('heslo')
    print(login)
    with db_session:
        uzivatel = Uzivatel.get(login=login)
        if uzivatel:
            pwhash = uzivatel.heslo
        else:
            pwhash = None
    check_password_hash(pwhash, heslo)
    return render_template('base.html.j2')
