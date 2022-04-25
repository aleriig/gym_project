from flask import Blueprint, Flask, redirect, render_template, request

from models.sport_class import Sport_class
import repositories.sport_class_repository as sport_class_repository
import repositories.member_repository as member_repository

sport_classes_blueprint = Blueprint("sport_classes", __name__)

@sport_classes_blueprint.route("/sport_classes")
def sport_class():
    sport_classes = sport_class_repository.select_all()
    return render_template("sport_classes/index.html", sport_classes=sport_classes)

@sport_classes_blueprint.route("/sport_classes/new")
def new_sport_class():
    return render_template("sport_classes/new.html")

@sport_classes_blueprint.route("/sport_classes", methods=["POST"])
def create_sport_class():
    name = request.form['name']
    date = request.form["date"]
    duration = request.form["duration"]
    new_sport_class = Sport_class(name, date, duration)
    sport_class_repository.save(new_sport_class)
    return redirect("/sport_classes")

@sport_classes_blueprint.route("/sport_classes/<id>/edit")
def edit_sport_class(id):
    sport_class = sport_class_repository.select(id)
    return render_template("/sport_classes/edit.html", sport_class=sport_class)

@sport_classes_blueprint.route("/sport_classes/<id>", methods=["POST"])
def update_sport_class(id):
    name = request.form["name"]
    date = request.form["date"]
    duration = request.form["duration"]
    sport_class = Sport_class(name, date, duration, id)
    sport_class_repository.update(sport_class)
    return redirect("/sport_classes")