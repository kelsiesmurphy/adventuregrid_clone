from flask import Flask, Blueprint, redirect, render_template, request
from models.experience import Experience
import repositories.experience_repository as experience_repository

experiences_blueprint = Blueprint("experiences", __name__)


# INDEX
# GET '/experiences'
@experiences_blueprint.route('/experiences')
def experiences_home():
    experiences = experience_repository.select_all()
    return render_template('experiences/index.html', experiences=experiences)


# NEW EXPERIENCE
# GET '/experiences/new'
@experiences_blueprint.route('/experiences/new')
def experience_new():
    return render_template('experiences/create.html')


# CREATE EXPERIENCE
# POST '/experiences'
@experiences_blueprint.route('/experiences', methods=['POST'])
def experience_create():
    title = request.form['title']
    description = request.form['description']
    location = request.form['location']
    image = request.form['image']
    price = request.form['price']
    is_featured = 'is_featured' in request.form

    new_experience = Experience(title, description, location, image, price, is_featured)
    experience_repository.save(new_experience)
    return redirect('/experiences')


# SHOW EXPERIENCE
# GET '/experiences/<id>'
@experiences_blueprint.route('/experiences/<int:id>')
def experience_show(id):
    experience = experience_repository.select_by_id(id)
    users = experience_repository.users(experience)
    return render_template('experiences/show.html', experience=experience, users=users)


# EDIT EXPERIENCE
# GET '/experiences/<id>/edit'
@experiences_blueprint.route('/experiences/<int:id>/edit')
def experience_edit(id):
    experience = experience_repository.select_by_id(id)
    return render_template('experiences/edit.html', experience = experience)


# UPDATE EXPERIENCE
# POST '/experiences/<id>' (would normally be PUT)
@experiences_blueprint.route('/experiences/<int:id>', methods=['POST'])
def experience_update(id):
    title = request.form['title']
    description = request.form['description']
    location = request.form['location']
    image = request.form['image']
    price = request.form['price']
    is_featured = 'is_featured' in request.form

    updated_experience = Experience(title, description, location, image, price, is_featured, id)
    experience_repository.update(updated_experience)
    return redirect(f'/experiences/{updated_experience.id}')


# DELETE EXPERIENCE
# DELETE '/experiences/<id>/delete'
@experiences_blueprint.route('/experiences/<int:id>/delete', methods=["POST"])
def experience_delete(id):
    experience_repository.delete_by_id(id)
    return redirect('/experiences')