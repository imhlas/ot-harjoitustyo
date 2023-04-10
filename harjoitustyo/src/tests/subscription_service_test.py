import unittest
from entities.user import User
from services.subscription_service import (SubscriptionService, UsernameExistsError, InvalidCredentialsError)

class FakeUserRepository:
    #tallennetaan testauksessa käyttäjät listaan, jotta tietokantayhteyttä ei tarvita service-koodin testauksessa
    def __init__(self):
        self.users = []

    def get_users(self):
        if len(self.users) >= 1:
             all_usernames = []
             for user in self.users:
                 all_usernames.append(user.username)
                 return all_usernames
        return []

    def create_user(self, user):
        self.users.append(user)

    def find_user(self, username, password):
        for row in self.users:
            if username == self.users[0] and password == self.users[1]:
                return (self.users[0], self.users[1])
        return None

class TestSubscriptionService(unittest.TestCase):
    def setUp(self):
        self.subscription_service = SubscriptionService(FakeUserRepository())
        self.user_timo = User("timo", "salasana123")

    def test_create_user_succesfully(self):
        username = self.user_timo.username
        password = self.user_timo.password

        self.subscription_service.create_user(username, password)

        all_usernames = self.subscription_service.return_all_users()

        self.assertEqual(len(all_usernames), 1)
        self.assertEqual(all_usernames[0], username)
