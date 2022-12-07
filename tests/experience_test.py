import unittest
from models.experience import Experience
from models.user import User
from models.users_experiences import Users_Experiences

import repositories.experience_repository as experience_repository
import repositories.user_repository as user_repository
import repositories.users_experience_repository as users_experience_repository


class TestExperience(unittest.TestCase):
    def setUp(self):
        self.experience1 = Experience("The Highland Trail", "Take in the Scottish highlands as you travel on the Jacobite Steam Train over the Glenfinnan Viaduct.", "West Highlands, Scotland", "/static/images/experiences/highland_trail.jpg", 5, False)
        self.experience2 = Experience("Obscure Edinburgh", "From the old town of Edinburgh to the hidden gems of Leith, explore the city and learn about its rich history.", "Edinburgh, Scotland", "/static/images/experiences/edinburgh.jpg", 5, True)

    def test_experience_has_title(self):
        self.assertEqual("The Highland Trail", self.experience1.title)

    def test_experience_has_price(self):
        self.assertEqual(5, self.experience2.price)