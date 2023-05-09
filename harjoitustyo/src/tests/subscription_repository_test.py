import unittest
from entities.subscription import Subscription
from entities.user import User
from repositories.subscription_repository import subscription_repository
from initialize_database import initialize_database
from datetime import datetime

class TestSubscriptionRepository(unittest.TestCase):
    def setUp(self):
        self.kayttaja1 = User("iida", "salasana123")

        self.subscription1 = Subscription(self.kayttaja1.user_id, "Netflix", 9.90, "3.3.2023")
        self.subscription2 = Subscription(self.kayttaja1.user_id, "Spotify", 11.90, "2.2.2022")
        initialize_database()

    def test_create(self):
        subscription = subscription_repository.create(self.subscription1)

        self.assertEqual(subscription.user_id, self.kayttaja1.user_id)
        self.assertEqual(subscription.name, "Netflix")
        self.assertEqual(subscription.price, 9.90)
        self.assertEqual(subscription.end_date, "3.3.2023")

    def test_find_users_subscriptions_returns_all_subscriptions(self):
        subscription_repository.create(self.subscription1)
        subscription_repository.create(self.subscription2)

        subscriptions = subscription_repository.find_users_subscriptions(self.kayttaja1)

        self.assertEqual(len(subscriptions), 2)

        self.assertEqual(subscriptions[0].name, "Netflix")
        self.assertEqual(subscriptions[1].name, "Spotify")

    def test_find_users_subscriptions_returns_None(self):
        subscriptions = subscription_repository.find_users_subscriptions(self.kayttaja1)

        self.assertEqual(subscriptions, None)

    def test_update_subscription_state_to_ending(self):
        subscription_repository.create(self.subscription1)
        subscriptions = subscription_repository.find_users_subscriptions(self.kayttaja1)


        self.assertEqual(len(subscriptions), 1)
        self.assertEqual(subscriptions[0].state, "active")

        subscription_repository.update_state_ending(subscriptions[0].subscription_id)

        subscriptions = subscription_repository.find_users_subscriptions(self.kayttaja1)

        self.assertEqual(len(subscriptions), 1)
        self.assertEqual(subscriptions[0].state, "ending")

    def test_update_subscription_state_to_ended(self):
        pass



