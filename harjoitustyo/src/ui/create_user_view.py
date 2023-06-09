from tkinter import ttk, constants, StringVar
from services.subscription_service import subscription_service, UsernameExistsError


class CreateUserView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä."""

    def __init__(self, root, show_login_view):
        """Luokan konstruktori, mikä luo uuden rekisteröitymisnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            show_login_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään kirjautumisnäkymään.
        """

        self._root = root
        self._show_login_view = show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""

        self._frame.place(relx=0.5, rely=0.5, anchor='center')

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def _create_user_handler(self):
        """Noutaa syötteet käyttäjätunnuksen ja salasanan kentistä ja yrittää luoda niistä uuden käyttäjän.
           Tuottaa virheen, mikäli käyttäjätunnus on jo olemassa."""

        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        try:
            subscription_service.create_user(username_value, password_value)
            self._show_message(f"User created succesfully. Please wait.")
            self._root.after(3000, self._show_login_view)

        except UsernameExistsError:
            self._show_message(f"Username {username_value} already exists")

    def _show_message(self, message):
        """Näyttää halutun viestin näkymässä."""

        self._message_variable.set(message)
        self._message_label.grid()

    def _initialize_username_and_password_field(self):
        """Alustaa näkymään kentät käyttäjätunnuksen ja salasanan syötteille"""

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky=constants.EW)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, pady=5)
        self._password_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky= constants.EW)

    def _initialize(self):
        """Alustaa näkymän."""

        self._frame = ttk.Frame(master=self._root)

        self._message_variable = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame, textvariable=self._message_variable, font=("Arial", 12, "bold"))

        self._message_label.grid(row=5, column=0, columnspan=3, pady=5)

        heading_label = ttk.Label(
            master=self._frame, text="Create user", font=("Arial", 13))
        heading_label.grid(row=0, column=1, sticky=constants.NSEW, pady=5)

        self._initialize_username_and_password_field()

        login_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_login_view)
        create_user_button = ttk.Button(
            master=self._frame, text="Create user", command=self._create_user_handler)

        login_button.grid(row=3, column=1, padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(row=3, column=2, padx=5, pady=5, sticky = constants.EW)
