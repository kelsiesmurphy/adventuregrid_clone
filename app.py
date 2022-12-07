from flask import Flask, render_template
import random
from controllers.experience_controller import experiences_blueprint
from controllers.users_experiences_controller import users_experiences_blueprint
from controllers.user_controller import users_blueprint

from repositories import experience_repository, user_repository, users_experience_repository

app = Flask(__name__)
app.register_blueprint(users_experiences_blueprint)
app.register_blueprint(experiences_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def index():
    experiences = experience_repository.select_all()

    featured_experiences = []
    for experience in experiences:
        if experience.is_featured == True:
            featured_experiences.append(experience)
    featured_experience = featured_experiences[random.randint(0, len(featured_experiences)-1)]
    users = user_repository.select_all()
    reviews = users_experience_repository.select_all()
    review = reviews[random.randint(0, len(reviews)-1)]
    return render_template('index.html', experiences=experiences, users=users, review=review, featured_experience=featured_experience)

@app.route('/dashboard')
def home():
    experiences = experience_repository.select_all()
    users = user_repository.select_all()
    return render_template('dashboard.html', experiences=experiences, users=users)

if __name__ == '__main__':
    app.run(debug=True)