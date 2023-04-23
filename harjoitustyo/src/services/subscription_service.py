from entities.user import User
from entities.subscription import Subscription

from repositories.user_repository import (
    user_repository as default_user_repository)

from repositories.subscription_repository import (
    subscription_repository as default_subscription_repository)

# omat luokat erroreille, jotta ne voidaan importata suoraan testeihin
class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class SubscriptionService:
    def __init__(self, user_repository=default_user_repository,
        subscription_repository = default_subscription_repository):

        self._user = None
        # default_user_repo mahdollistaa tietokantayhteyden luonnin repon puolella
        self._user_repository = user_repository
        self._subscription_repository = subscription_repository

    def create_user(self, username, password):
        all_users = self._user_repository.get_users()
        if username not in all_users:
            self._user_repository.create_user(User(username, password))
        else:
            raise UsernameExistsError(f"Username {username} already exists")

    def login(self, username, password):
        user_info = self._user_repository.find_user(username, password)

        if not user_info:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user_info

        return user_info

    def return_all_users(self):
        all_users = self._user_repository.get_users()
        return all_users

    def return_current_user(self):
        return self._user

    def create_subscription(self, name, price, end_date):
        subscription = Subscription(user_id=self._user.user_id, name=name,
            price=price, end_date=end_date)

        return self._subscription_repository.create(subscription)

    def get_subscriptions(self):
        if not self._user:
            return []

        subscriptions = self._subscription_repository.find_users_subscriptions(self._user)

        return subscriptions

    def logout(self):
        self._user = None

subscription_service = SubscriptionService()
