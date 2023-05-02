from datetime import datetime
from entities.subscription import Subscription
from database_connection import get_database_connection

def database_rows_into_subscriptions(rows):
    subscriptions = []

    for row in rows:
        subscription = Subscription(row["user_id"], row["name"], row["price"], row["end_date"])
        subscriptions.append(subscription)

    return subscriptions

class SubscriptionRepository:
    """Luokka, jonka avulla hoidetaan tilauksiin liittyviä tietokantaoperaatioita.

    Attributes:
        connection: Tietokantayhteyden Connection-olio.
    """


    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def find_users_subscriptions(self, user):
        """Palauttaa käyttäjän tilaukset.

        Args:
            user: User-olio, jonka tilaukset palautetaan.

        Returns:
            Palauttaa listan Subscription-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM subscriptions  WHERE user_id=?", (user.user_id,))
        rows = cursor.fetchall()

        if len(rows) == 0:
            return None
        return database_rows_into_subscriptions(rows)

    def create(self, subscription):
        """Tallentaa tilauksen tietokantaan.

        Args:
            subscription: Tallennettava tilaus Subscription-oliona.

        Returns:
            Tallennettu tilaus Subsription-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO subscriptions (user_id, name, price, end_date) values (?, ?, ?, ?)",
            (subscription.user_id, subscription.name, subscription.price,
            datetime.strptime(subscription.end_date, "%d.%m.%Y")))

        self._connection.commit()

        return subscription

subscription_repository = SubscriptionRepository(get_database_connection())
