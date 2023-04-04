import unittest
from entities.user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection
from initialize_database import initialize_database

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.kayttaja1 = User("iida", "salasana123")
        self.kayttaja2 = User("timo", "testword456")
        initialize_database()
        connection = get_database_connection()
        self.user_repo = UserRepository(connection)

    def test_user_can_be_created(self):
        self.user_repo.create_user(self.kayttaja1)
        self.user_repo.create_user(self.kayttaja2)

        all_users = self.user_repo.get_users()

        self.assertEqual(all_users, ["iida", "timo"])

    def test_find_user_returns_user_info(self):
        self.user_repo.create_user(self.kayttaja1)
        user_info = self.user_repo.find_user("iida", "salasana123")
        self.assertEqual(user_info, ("iida", "salasana123"))

    def test_find_user_returns_none_if_no_user(self):
        #käyttäjää ei ole luotu tietokantaan, joten funktion tulisi palauttaa None
        user_info = self.user_repo.find_user("iida", "salasana123")

        self.assertEqual(user_info, None)
