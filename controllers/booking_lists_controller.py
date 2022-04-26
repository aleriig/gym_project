from flask import Blueprint, Flask, redirect, render_template, request

from models.booking_list import Booking_list
import repositories.booking_list_repository as booking_list_repository
import repositories.member_repository as member_repository
import repositories.sport_class_repository as sport_class_repository

booking_lists_blueprint = Blueprint("booking_lists", __name__)

@booking_lists_blueprint.route("/booking_lists")
def booking_lists():
    booking_lists = booking_list_repository.select_all()
    return render_template("booking_lists/index.html", booking_lists=booking_lists)

@booking_lists_blueprint.route("/booking_lists/new")
def new_booking():
    members = member_repository.select_all()
    sport_classes = sport_class_repository.select_all()
    return render_template("booking_lists/new.html", members=members, sport_classes=sport_classes)

@booking_lists_blueprint.route("/booking_lists", methods= ["POST"])
def create_booking():
    member_id = request.form["member_id"]
    sport_class_id = request.form["sport_class_id"]
    member = member_repository.select(member_id)
    sport_class = sport_class_repository.select(sport_class_id)
    new_booking = Booking_list(member, sport_class)
    booking_list_repository.save(new_booking)
    return redirect("/booking_lists")

@booking_lists_blueprint.route("/booking_lists/<id>/edit")
def edit_booking(id):
    booking_list = booking_list_repository.select(id)
    members = member_repository.select_all()
    sport_classes = sport_class_repository.select_all()
    return render_template("booking_lists/edit.html", booking_list=booking_list, members=members, sport_classes=sport_classes)

@booking_lists_blueprint.route("/booking_lists/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form['member_id']
    sport_class_id = request.form["sport_class_id"]
    member = member_repository.select(member_id)
    sport_class = sport_class_repository.select(sport_class_id)
    booking = Booking_list(member, sport_class, id)
    booking_list_repository.update(booking)
    return redirect("/booking_lists")

# @booking_lists_blueprint.route("/booking_lists/<id>/delete" methods = ["POST"])
# def delete_