from flask import Blueprint, Flask, redirect, render_template, request

from models.sport_class import Sport_class
import repositories.sport_class_repository as sport_class_repository
import repositories.member_repository as member_repository

sport_classes_blueprint = Blueprint("sport_classes", __name__)
