from models.experience import Experience
from models.user import User
from models.users_experiences import Users_Experiences

import repositories.experience_repository as experience_repository
import repositories.user_repository as user_repository
import repositories.users_experience_repository as users_experience_repository

user_repository.delete_all()
experience_repository.delete_all()
users_experience_repository.delete_all()

user1  = User("John Jones", "johnjones987", "johnjones@email.com", "/static/images/users/john.png")
user_repository.save(user1)

user2  = User("Jaida Shōta", "jaidashota453", "jaidashota@email.com", "/static/images/users/jaida.png")
user_repository.save(user2)

user3  = User("Viktor Atanasio", "viktoratan202", "viktoratan@email.com", "/static/images/users/viktor.png")
user_repository.save(user3)

user4  = User("Anni Eskil", "annieskil245", "annieskil@email.com", "/static/images/users/anni.png")
user_repository.save(user4)

user_repository.select_all()


experience1 = Experience("The Highland Trail", "Take in the Scottish highlands as you travel on the Jacobite Steam Train over the Glenfinnan Viaduct.", "West Highlands, Scotland", "/static/images/experiences/highland_trail.jpg", 5, False)
experience_repository.save(experience1)

experience2 = Experience("Obscure Edinburgh", "From the old town of Edinburgh to the hidden gems of Leith, explore the city and learn about its rich history.", "Edinburgh, Scotland", "/static/images/experiences/edinburgh.jpg", 5, True)
experience_repository.save(experience2)

experience3 = Experience("The Devils Pulpit", "Get your boots on and stay safe as you explore this deep sandstone gorge hidden in the middle of a forest", "Loch Lomond, Scotland", "/static/images/experiences/devils_pulpit.jpg", 5, False)
experience_repository.save(experience3)

experience4 = Experience("Glencoe Valley", "Carved out centuries ago by icy glaciers and volcanic explosions, Glencoe is a beautiful place to explore.", "Glencoe, Scotland", "/static/images/experiences/glencoe.jpg", 5, False)
experience_repository.save(experience4)

experience5 = Experience("Hidden Glasgow", "From the Glasgow Necropolis to the life of the Glasgow architect Charles Rennie Mackintosh, there's plenty to do.", "Glasgow, Scotland", "/static/images/experiences/glasgow.jpg", 0, False)
experience_repository.save(experience5)

experience6 = Experience("Skye's Secret", "Skye is a truly magical place to visit and home to some of Scotland’s most inspiring landscapes.", "Skye, Scotland", "/static/images/experiences/skye.jpg", 5, False)
experience_repository.save(experience6)

experience_repository.select_all()


review1 = Users_Experiences(user1, experience1, "I've lived in Scotland for ten years and I feel like i’m rediscovering it all over again!")
users_experience_repository.save(review1)

review2 = Users_Experiences(user2, experience2, "I live in Edinburgh and AdventureGrid has shown me parts of the city i've never seen!")
users_experience_repository.save(review2)

review3 = Users_Experiences(user3, experience3, "I like it")
users_experience_repository.save(review3)

users_experience_repository.select_all()

