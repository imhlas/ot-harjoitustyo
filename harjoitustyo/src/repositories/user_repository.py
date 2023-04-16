from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_users(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM  users")
        rows = cursor.fetchall()
        # palauttaa pelkät käyttäjätunnukset ilman salasanatietoja
        return [row["username"] for row in rows]

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)",
                       (user.user_id, user.username, user.password))
        self._connection.commit()

        return user

    def find_user(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password))
        row = cursor.fetchone()

        # Jos käyttäjää ei löydy, funktio palauttaa None
        return (row["user_id"], row["username"], row["password"]) if row else None

user_repository = UserRepository(get_database_connection())
