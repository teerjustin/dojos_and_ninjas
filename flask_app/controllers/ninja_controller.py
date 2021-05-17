from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.ninja import Ninja
from ..models.dojo import Dojo


@app.route("/ninjas")
def display_create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/ninjas", methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)
    dojo_id = request.form['dojo_id']
    redirectString = "../dojos/" + dojo_id
    return redirect(redirectString)