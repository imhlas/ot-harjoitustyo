from entities.user import User
from repositories.user_repository import UserRepository

class SubscriptionService:
    def __init__(self):
	#UserReposity -luokkaa käytetään tässä vaiheessa käyttäjien tallennuspaikkana
	#Tämä korvataan myöhemmin tietokantayhteydellä
        self.user_repository = UserRepository()

    def create_user(self, username, password):
	all_users = self.user_repository.get_users()
	if username not in  all_users:
	    self.user_repository.add_user_to_userlist(User(username, password))
	else:
	    raise UsernameExistsError(f"Username {username} already exists")

