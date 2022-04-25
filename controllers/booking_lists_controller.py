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