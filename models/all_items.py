from models.experience import Experience
from models.user import User
from models.users_experiences import Users_Experiences


user1  = User("John Jones", "johnjones987", "johnjones@email.com", "/static/images/users/john.png")
user2  = User("Jaida Shōta", "jaidashota453", "jaidashota@email.com", "/static/images/users/jaida.png")
user3  = User("Viktor Atanasio", "viktoratan202", "viktoratan@email.com", "/static/images/users/viktor.png")
user4  = User("Anni Eskil", "annieskil245", "annieskil@email.com", "/static/images/users/anni.png")

all_users = [user1, user2, user3, user4]


experience1 = Experience("The Highland Trail", "Take in the Scottish highlands as you travel on the Jacobite Steam Train over the Glenfinnan Viaduct.", "West Highlands, Scotland", "/static/images/experiences/highland_trail.jpg", 5, False)
experience2 = Experience("Obscure Edinburgh", "From the old town of Edinburgh to the hidden gems of Leith, explore the city and learn about its rich history.", "Edinburgh, Scotland", "/static/images/experiences/edinburgh.jpg", 5, True)
experience3 = Experience("The Devils Pulpit", "Get your boots on and stay safe as you explore this deep sandstone gorge hidden in the middle of a forest", "Loch Lomond, Scotland", "/static/images/experiences/devils_pulpit.jpg", 5, False)
experience4 = Experience("Glencoe Valley", "Carved out centuries ago by icy glaciers and volcanic explosions, Glencoe is a beautiful place to explore.", "Glencoe, Scotland", "/static/images/experiences/glencoe.jpg", 5, False)
experience5 = Experience("Hidden Glasgow", "From the Glasgow Necropolis to the life of the Glasgow architect Charles Rennie Mackintosh, there's plenty to do.", "Glasgow, Scotland", "/static/images/experiences/glasgow.jpg", 0, False)
experience6 = Experience("Skye's Secret", "Skye is a truly magical place to visit and home to some of Scotland’s most inspiring landscapes.", "Skye, Scotland", "/static/images/experiences/skye.jpg", 5, False)

all_experiences = [experience1, experience2, experience3, experience4]


review1 = Users_Experiences(user1, experience1, "I've lived in Scotland for ten years and I feel like i’m rediscovering it all over again!")
review2 = Users_Experiences(user2, experience2, "I live in Edinburgh and AdventureGrid has shown me parts of the city i've never seen!")
review3 = Users_Experiences(user3, experience3, "I like it")

all_reviews = [review1, review2, review3]