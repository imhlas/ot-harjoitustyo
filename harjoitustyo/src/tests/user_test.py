import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_kayttajan_luonti_onnistuu(self):
        # alustetaan kayttaja, jolle määritetään käyttäjänimi ja salasana
        kayttaja1 = User("iida", "salasana123")

        self.assertEqual(kayttaja1.password, "salasana123")
