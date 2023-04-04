from entities.user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection

class SubscriptionService:
    def __init__(self):
	#UserReposity -luokkaa käytetään käyttäjiin liittyvissä tietokantaoperaatioissa
        connection = get_database_connection()
        self.user_repository = UserRepository(connection)

    def create_user(self, username, password):
        all_users = self.user_repository.get_users()
        if username not in  all_users:
            self.user_repository.create_user(User(username, password))
        else:
            raise UsernameExistsError(f"Username {username} already exists")

    def login(self, username, password):
        user_info = self.user_repository.find_user(username, password)
        if not user_info:
            raise InvalidCredentialsError("Invalid username or password")
        else:
            user = User(user_info[0], user_info[1])
        return user
