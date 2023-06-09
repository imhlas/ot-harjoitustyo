from tkinter import ttk, constants, StringVar
from services.subscription_service import subscription_service


class CreateSubscriptionView:
    """Uuden tilauksen luonnista vastaava näkymä."""

    def __init__(self, root, show_application_view):
        """Luokan konstruktori, mikä luo uuden näkymän tilauksen luonnille.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            show_application_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään tilauksien listausnäkymään.
        """

        self._root = root
        self._show_application_view = show_application_view
        self._frame = None
        self._subscription_name_entry = None
        self._subscription_price_entry = None
        self._end_date_entry = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def _create_subscription_handler(self):
        """Noutaa syötteet tilauksen tiedoista vastaavista kentistä ja luo niistä uuden tilauksen.
           Siirtää tämän jälkeen näkymän automaattisesti takaisin tilauksien listausnäkymään"""


        subscription_name_value = self._subscription_name_entry.get()
        subscription_price_value = self._subscription_price_entry.get()
        end_date_value = self._end_date_entry.get()

        try:
            price_float = float(subscription_price_value)
        except ValueError:
            self._show_message("Wrong format in price input")

        try:
            subscription_service.create_subscription(subscription_name_value, price_float,
                end_date_value)
            self._show_message(f"New subscription added succesfully.Please wait.")

            self._root.after(3000, self._show_application_view)
        except Exception:
            self._show_message("Invalid input fields")

    def _show_message(self, message):
        """Näyttää halutun viestin näkymässä."""


        self._message_variable.set(message)
        self._message_label.grid()

    def _initialize_fields(self):
        """Alustaa näkymään kentät tilauksen tietojen syötteille"""

        subscription_name_label = ttk.Label(master=self._frame, text="Subscription name")
        self._subscription_name_entry = ttk.Entry(master=self._frame)

        subscription_name_label.grid(row=1, column=0)
        self._subscription_name_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=constants.EW)

        subscription_price_label = ttk.Label(master=self._frame, text="Monthly price (xx.xx)")
        self._subscription_price_entry = ttk.Entry(master=self._frame)

        subscription_price_label.grid(row=2, column=0)
        self._subscription_price_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=constants.EW)

        end_date_label = ttk.Label(master=self._frame, text="End date (dd.mm.yyy)")
        self._end_date_entry = ttk.Entry(master=self._frame)

        end_date_label.grid(row=3, column=0)
        self._end_date_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        """Alustaa näkymän."""

        self._frame = ttk.Frame(master=self._root)

        self._message_variable = StringVar(self._frame)
        self._message_label = ttk.Label(
            master=self._frame, textvariable=self._message_variable, font=("Arial", 12, "bold"))

        self._message_label.grid(row=5, column=0, columnspan=3, pady=5)

        heading_label = ttk.Label(master=self._frame, text="Add new subscription",
            font=("Arial", 14))
        heading_label.grid(row=0, column=1, sticky=constants.NSEW, pady=5)

        self._initialize_fields()

        cancel_button = ttk.Button(master=self._frame, text="Cancel",
            command=self._show_application_view)

        create_subscription_button = ttk.Button(master=self._frame, text="Add subscription",
            command=self._create_subscription_handler)

        cancel_button.grid(row=4, column=1, pady=5)
        create_subscription_button.grid(row=4, column=2, pady=5)
