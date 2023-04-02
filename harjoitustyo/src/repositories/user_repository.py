from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_users(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM  users")

        rows = cursor.fetchall()

        return [row[0] for row in rows]

    def create_user(self, user):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))

        self._connection.commit()

        return user
