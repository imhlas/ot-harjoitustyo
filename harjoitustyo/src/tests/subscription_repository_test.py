import unittest
from entities.subscription import Subscription
from repositories.subscription_repository import SubscriptionRepository
from database_connection import get_database_connection
from initialize_database import initialize_database
from datetime import datetime

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.subscription1 = Subscription("user_id1", "Netflix", 9.90, "3.3.2023")
        self.subscription2 = Subscription("user_id2", "Spotify", 11.90, "2.2.2022")
        initialize_database()
        connection = get_database_connection()
        self.subs_repo = SubscriptionRepository(connection)

    def test_create(self):
        subscription = self.subs_repo.create(self.subscription1)

        self.assertEqual(subscription.user_id, "user_id1")
        self.assertEqual(subscription.name, "Netflix")
        self.assertEqual(subscription.price, 9.90)
        self.assertEqual(subscription.end_date, "3.3.2023")
