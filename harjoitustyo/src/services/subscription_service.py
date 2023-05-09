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
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, user_repository=default_user_repository,
        subscription_repository = default_subscription_repository):

        """Luokan konstruktori, mikä luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            subscription_repository:
                Vapaaehtoinen, oletusarvoltaan SubscriptionRepository-olio.
                Olio, jolla on SubscriptionRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """

        self._user = None
        # default_user_repo mahdollistaa tietokantayhteyden luonnin repon puolella
        self._user_repository = user_repository
        self._subscription_repository = subscription_repository

    def create_user(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.

        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.

        Returns:
            Luotu käyttäjä User-oliona.
        """

        all_users = self._user_repository.get_users()
        if username not in all_users:
            self._user_repository.create_user(User(username, password))
        else:
            raise UsernameExistsError(f"Username {username} already exists")

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-oliona.
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun käyttäjätunnus tai salasana ei täsmää.
        """

        user_info = self._user_repository.find_user(username, password)

        if not user_info:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user_info

        return user_info

    def return_all_users(self):
        """Palauttaa listan kaikista käytössä olevista käyttäjätunnuksista. """

        all_users = self._user_repository.get_users()
        return all_users

    def return_current_user(self):
        """Palauttaa nykyisen käyttäjän User-oliona. """

        return self._user

    def create_subscription(self, name, price, end_date):
        """Luo uuden tilauksen.

        Args:
            name: Tilauksen nimi.
            price: Tilauksen hinta.
            end_date: Tilauksen päättymispäivä
        Returns:
            Luotu tilaus Subscription-oliona.
        """

        subscription = Subscription(user_id=self._user.user_id, name=name,
            price=price, end_date=end_date)

        return self._subscription_repository.create(subscription)

    def get_subscriptions(self):
        """Palauttaa kirjautuneen käyttäjän tilaukset.

        Returns:
            Palauttaa kirjautuneen käyttäjän tilaukset Subscription-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self._user:
            return []

        subscriptions = self._subscription_repository.find_users_subscriptions(self._user)

        return subscriptions

    def get_sum_of_subscriptions(self, subscriptions):
        """Palauttaa tilauksien summan.

        Args:
            subscriptions: Lista tilauksista Subscription-olioina.
        Returns:
            Tilauksien summa.
        """


        sum = 0
        for subscription in subscriptions:
            sum += subscription.price

        return sum

    def set_subscription_ending(self, subscription_id):
        """Päivittää tilauksen päättyväksi.
        """

        self._subscription_repository.update_state_ending(subscription_id)


    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos. """

        self._user = None

subscription_service = SubscriptionService()
