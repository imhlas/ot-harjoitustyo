import uuid

class User:
    """Luokka, joka kuvaa käyttäjää.

    Attributes:
        username: Käyttäjän käyttäjätunnus.
        password: Käyttäjän salasana.
        user_id: Käyttäjän tunniste.
    """
    def __init__(self, username, password, user_id=None):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Käyttäjän käyttäjätunnus.
            password: Käyttäjän salasana.
            user_id: Käyttäjän tunniste.
        """
        self.username = username
        self.password = password
        self.user_id = user_id or str(uuid.uuid4())
