import unittest
from entities.user import User
from entities.subscription import Subscription
from services.subscription_service import (
    SubscriptionService, UsernameExistsError, InvalidCredentialsError)


class FakeUserRepository:
    # tallennetaan testauksessa käyttäjät listaan, jotta tietokantayhteyttä ei tarvita service-koodin testauksessa
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
            if username == row.username and password == row.password:
                return row
        return None

class FakeSubscriptionRepository:
    def __init__(self):
        self.subscriptions = []

    def create(self, subscription):
        self.subscriptions.append(subscription)
        return self.subscriptions[0]

    def find_users_subscriptions(self, user):
        users_subscriptions = []

        for row in self.subscriptions:
            if row.user_id == user.user_id:
                users_subscriptions.append(row)

        return users_subscriptions

class TestSubscriptionService(unittest.TestCase):
    def setUp(self):
        self.subscription_service = SubscriptionService(FakeUserRepository(),FakeSubscriptionRepository())
        self.username = "timo"
        self.password = "salasana123"

    def test_create_user_succesfully(self):
        self.subscription_service.create_user(self.username, self.username)

        all_usernames = self.subscription_service.return_all_users()

        self.assertEqual(len(all_usernames), 1)
        self.assertEqual(all_usernames[0], self.username)

    def test_login_succesfully(self):
        self.subscription_service.create_user(self.username, self.password)
        user = self.subscription_service.login(self.username, self.password)

        self.assertEqual(user.username, self.username)
        self.assertEqual(user.password, self.password)

    def test_create_subscription(self):
        self.subscription_service.create_user(self.username, self.password)
        self.subscription_service.login(self.username, self.password)

        subscription = self.subscription_service.create_subscription("Netflix", 9.90, "5.5.2023")

        self.assertEqual(subscription.name, "Netflix")
        self.assertEqual(subscription.price, 9.90)
        self.assertEqual(subscription.end_date, "5.5.2023")

    def test_get_subscriptions(self):
        self.subscription_service.create_user(self.username, self.password)
        self.subscription_service.login(self.username, self.password)

        subscription1 = self.subscription_service.create_subscription("Netflix", 9.90, "5.5.2023")
        subscription2 = self.subscription_service.create_subscription("Spotify", 11.90, "6.6.2023")

        subscriptions = self.subscription_service.get_subscriptions()

        self.assertEqual(len(subscriptions), 2)
        self.assertEqual(subscriptions[0].name, "Netflix")
        self.assertEqual(subscriptions[1].price, 11.90)

