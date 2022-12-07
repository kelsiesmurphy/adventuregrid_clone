from flask import Flask, Blueprint, redirect, render_template, request
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)


# INDEX
# GET '/users'
@users_blueprint.route('/users')
def users_home():
    users = user_repository.select_all()
    return render_template('users/index.html', users=users)


# NEW USER
# GET '/users/new'
@users_blueprint.route('/users/new')
def users_new():
    return render_template('users/create.html')


# CREATE USER
# POST '/users'
@users_blueprint.route('/users', methods=['POST'])
def user_create():
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    image = request.form['image']

    new_user = User(name, email, username, image)
    user_repository.save(new_user)
    return redirect('/users')


# SHOW USER
# GET '/users/<id>'
@users_blueprint.route('/users/<int:id>')
def user_show(id):
    user = user_repository.select_by_id(id)
    experiences = user_repository.experiences(user)
    return render_template('users/show.html', user=user, experiences=experiences)


# EDIT USER
# GET '/users/<id>/edit'
@users_blueprint.route('/users/<int:id>/edit')
def users_edit(id):
    user = user_repository.select_by_id(id)
    return render_template('users/edit.html', user=user)


# UPDATE USER
# POST '/users/<id>' (would normally be PUT)
@users_blueprint.route('/users/<int:id>', methods=['POST'])
def user_update(id):
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    image = request.form['image']

    updated_user = User(name, email, username, image, id)
    user_repository.update(updated_user)
    return redirect(f'/users/{updated_user.id}')


# DELETE USER
# DELETE '/users/<id>/delete'
@users_blueprint.route('/users/<int:id>/delete', methods=["POST"])
def users_delete(id):
    user_repository.delete_by_id(id)
    return redirect('/users')