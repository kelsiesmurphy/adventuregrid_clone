from flask import Flask, Blueprint, redirect, render_template, request
from models.users_experiences import Users_Experiences
import repositories.users_experience_repository as users_experiences_repository

users_experiences_blueprint = Blueprint("users_experiences", __name__)


# INDEX
# GET '/reviews'
@users_experiences_blueprint.route('/reviews')
def users_experiences_home():
    users_experiences = users_experiences_repository.select_all()
    return render_template('reviews.html', users_experiences=users_experiences)