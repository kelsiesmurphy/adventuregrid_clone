import unittest
from models.experience import Experience
from models.user import User
from models.users_experiences import Users_Experiences

import repositories.experience_repository as experience_repository
import repositories.user_repository as user_repository
import repositories.users_experience_repository as users_experience_repository


class TestUsersExperiences(unittest.TestCase):
    def setUp(self):
        pass