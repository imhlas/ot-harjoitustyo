from tkinter import Tk
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.application_view import CreateApplicationView
from ui.create_subscription_view import CreateSubscriptionView

class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori, mika luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root: TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""

        self._show_login_view()

    def _hide_current_view(self):
        """Sulkee tämänhetkisen näkymän."""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        """Avaa kirjautumisnäkymän"""

        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_application_view, self._handle_create_user_view)

        self._current_view.pack()

    def _handle_create_user_view(self):
        """Avaa uuden käyttäjän luonnista vastaavan näkymän"""

        self._hide_current_view()

        self._current_view = CreateUserView(self._root, self._show_login_view)

        self._current_view.pack()

    def _show_application_view(self):
        """Avaa sovelluksen päänäkymän, eli tilausnäkymän"""

        self._hide_current_view()

        self._current_view = CreateApplicationView(self._root, self._show_login_view,
            self._show_create_subscription_view)

        self._current_view.pack()


    def _show_create_subscription_view(self):
        """Avaa uuden tilauksen luonnista vastaavan näkymän"""

        self._hide_current_view()

        self._current_view = CreateSubscriptionView(self._root, self._show_application_view)

        self._current_view.pack()
