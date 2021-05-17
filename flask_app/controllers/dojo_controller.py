from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.dojo import Dojo

#display home page... show all dojos/ option to create dojo
@app.route("/")
def index():
    return redirect("/dojos")

# show dojo and the ninjas inside dojo
@app.route("/dojos/<int:dojo_id>")
def display_dojo_with_ninjas(dojo_id):
    this_dojo = Dojo.get_dojo_with_ninjas({"id": dojo_id})
    return render_template('show.html', dojo = this_dojo)
    
# show all dojos
@app.route("/dojos")
def display_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html", dojos = dojos)



# create dojo on home screen
@app.route("/dojos", methods = ["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect("/")










