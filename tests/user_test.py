import unittest
from models.experience import Experience
from models.user import User
from models.users_experiences import Users_Experiences

import repositories.experience_repository as experience_repository
import repositories.user_repository as user_repository
import repositories.users_experience_repository as users_experience_repository


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1  = User("John Jones", "johnjones@email.com", "johnjones987", "/static/images/users/john.png")
        self.user2  = User("Jaida Shōta", "jaida@email.com", "jaidashota453", "/static/images/users/jaida.png")


    def test_user_has_name(self):
        self.assertEqual("John Jones", self.user1.name)

    def test_user_has_email(self):
        self.assertEqual("jaida@email.com", self.user2.email)