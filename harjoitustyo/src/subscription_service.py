from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)


class SubscriptionService:
    def __init__(self, user_repository = default_user_repository):
	#default_user_repo mahdollistaa tietokantayhteyden luonnin repon puolella
        self.user_repository = user_repository

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

    def return_all_users(self):
        all_users = self.user_repository.get_users()
        return all_users

#omat luokat erroreille, jotta ne voidaan importata suoraan testeihin
class UsernameExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass
