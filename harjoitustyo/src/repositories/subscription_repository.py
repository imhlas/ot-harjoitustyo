from datetime import datetime
from database_connection import get_database_connection

class SubscriptionRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_users_subscriptions(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM subscriptions  WHERE user_id=?", (user.user_id))
        rows = cursor.fetchall()

        return [list(row[1:]) for row in rows]

    def create(self, subscription):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO subscriptions (user_id, name, price, end_date) values (?, ?, ?, ?)",
            (subscription.user_id, subscription.name, subscription.price, datetime.strptime(subscription.end_date, "%d.%m.%Y"))
        )

        self._connection.commit()

        return subscription

subscription_repository = SubscriptionRepository(get_database_connection())
