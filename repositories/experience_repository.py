from db.run_sql import run_sql
from models.experience import Experience
from models.user import User

from models.all_items import all_experiences


# SAVE (Create in CRUD)
def save(experience):
    # sql = "INSERT INTO experiences (title, description, location, image, price, is_featured) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    # values = [experience.title, experience.description, experience.location, experience.image, experience.price, experience.is_featured]
    # result = run_sql(sql, values)[0]
    # result_id = result['id']
    # experience.id = result_id
    all_experiences.append(experience)
    return experience


# SELECT BY ID (Read in CRUD)
def select_by_id(id):
    # selected_experience = None
    # sql = "SELECT * FROM experiences WHERE id=%s"
    # values = [id]
    # result = run_sql(sql, values)[0]

    # if result is not None:
    #     selected_experience = Experience(result["title"], result["description"], result["location"], result["image"], result["price"], result["is_featured"], result["id"])
    for experience in all_experiences:
        if experience.id == id:
            return experience


# SELECT ALL
def select_all():
    selected_experiences = []
    sql = "SELECT * FROM experiences"
    results = run_sql(sql)
    for row in results:
        new_experience = Experience(row["title"], row["description"], row["location"], row["image"], row["price"], row["is_featured"], row["id"])
        selected_experiences.append(new_experience)
    return selected_experiences


# UPDATE (Update in CRUD)
def update(experience):    
    sql = "UPDATE experiences SET (title, description, location, image, price, is_featured) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [experience.title, experience.description, experience.location, experience.image, experience.price, experience.is_featured, experience.id]
    run_sql(sql, values)


# DELETE BY ID (Delete in CRUD)
def delete_by_id(id):
    # sql = "DELETE FROM experiences WHERE id = %s"
    # values = [id]
    # run_sql(sql, values)
    experience = select_by_id(id)
    all_experiences.remove(experience)


# DELETE ALL
def delete_all():
    sql = "DELETE FROM experiences"
    run_sql(sql)

# USERS RELATED TO EXPERIENCE
def users(experience):
    selected_users =[]
    sql = "SELECT users.* FROM users INNER JOIN users_experiences ON users_experiences.user_id=users.id WHERE experience_id=%s"
    values = [experience.id]
    results = run_sql(sql, values)
    for row in results:
        new_user = User(row["name"], row["email"], row["username"], row["image"], row["id"])
        selected_users.append(new_user)
    return selected_users