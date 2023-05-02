from database_connection import get_database_connection
from entities.user import User

class UserRepository:
    """Luokka, jonka avulla hoidetaan käyttäjiin liittyviä tietokantaoperaatioita.

    Attributes:
        connection: Tietokantayhteyden Connection-olio.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def get_users(self):
        """Palauttaa kaikki käyttäjätunnukset.

        Returns:
            Palauttaa listan käyttäjätunnuksia ilman salasanatietoja.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM  users")
        rows = cursor.fetchall()
        return [row["username"] for row in rows]

    def create_user(self, user):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä User-oliona.

        Returns:
            Tallennettu käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)",
                       (user.user_id, user.username, user.password))
        self._connection.commit()

        return user

    def find_user(self, username, password):
        """Palauttaa käyttäjän käyttäjätunnuksen sekä salasanan  perusteella.

        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.
            password: Salasana, jonka täytyy vastata käyttäjätunnuksen salasanaa.

        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen omaava käyttäjä on tietokannassa
            ja jos kyseisen käyttäjätunnuksen salasana vastaa syötettyä salasanaa.
            Muussa tapauksessa palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password))
        row = cursor.fetchone()

        return User(row["username"], row["password"], row["user_id"]) if row else None

user_repository = UserRepository(get_database_connection())
