from tkinter import ttk, constants
from datetime import datetime, timedelta
from services.subscription_service import subscription_service

class SubscriptionView:
    """Tilauksien listauksesta vastaava näkymä."""

    def __init__(self, root, subscriptions, handle_set_subscription_ending):
        """Luokan konstruktori, mikä luo uuden tilausnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            subscriptions:
                Lista Subscription-olioita, jotka näkymässä näytetään
            handle_set_subscription_ending;
                Kutsuttava arvo, jota kutsutaan, kun tilaus muutetaan päättyväksi.
        """

        self._root = root
        self._subscriptions = subscriptions
        self._handle_set_subscription_ending = handle_set_subscription_ending
        self._frame = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""

        self._frame.destroy()

    def _initialize_subscription_title(self):

        name_title = ttk.Label(
            master=self._frame, text="Subscription name", font=15)

        price_title = ttk.Label(master=self._frame,text="Subscription price",font=15)

        end_date_title = ttk.Label(master=self._frame,text="Next billing date",font=15)

        state_title = ttk.Label(master=self._frame, text="State", font=15)

        name_title.grid(row=0,column=0,columnspan=3,sticky=constants.EW,padx=5,pady=5)

        price_title.grid(row=0,column=3,columnspan=3,sticky=constants.EW,padx=5,pady=5)

        end_date_title.grid(row=0,column=6,columnspan=3,sticky=constants.EW,padx=5,pady=5)

        state_title.grid(row=0, column=9, columnspan=3, sticky=constants.EW, padx=5, pady=5)

    def _initialize_subscription(self, subscription, row):
        name_label = ttk.Label(master=self._frame, text=subscription.name)
        name_label.grid(row=row, column=0, columnspan=3, padx=5, pady=5, sticky=constants.W)

        price_label = ttk.Label(master=self._frame, text="{:.2f}€".format(float(subscription.price)).replace('.', ','))
        price_label.grid(row=row, column=3, columnspan=3, padx=5, pady=5, sticky=constants.W)

        if subscription.state == 'active':
            end_date = datetime.strptime(subscription.end_date, '%Y-%m-%d %H:%M:%S')
            billing_date = end_date + timedelta(days=1)
            billing_date_label = ttk.Label(master=self._frame, text=billing_date.strftime('%d-%m-%Y'))
            billing_date_label.grid(row=row, column=6, columnspan=3, padx=5, pady=5, sticky=constants.W)

            state_label = ttk.Label(master=self._frame, text=subscription.state.upper())
            state_label.grid(row=row, column=9, columnspan=3, padx=5, pady=5, sticky=constants.W)
            set_ending_button = ttk.Button(master=self._frame, text="Set ending",
                command=lambda:self._handle_set_subscription_ending(subscription.subscription_id))
            set_ending_button.grid(row=row, column=12, columnspan=2, padx=5, pady=5, sticky=constants.W)
        else:
            state_label = ttk.Label(master=self._frame, text= "ENDING ON:", foreground="red")
            state_label.grid(row=row, column=9, columnspan=3, padx=5, pady=5, sticky=constants.W)

            end_date = datetime.strptime(subscription.end_date, '%Y-%m-%d %H:%M:%S')
            end_date_label = ttk.Label(master=self._frame, text=end_date.strftime('%d-%m-%Y'), foreground="red")
            end_date_label.grid(row=row, column=12, columnspan=3, padx=5, pady=5, sticky=constants.W)

        self._frame.grid_columnconfigure(0, weight=10, minsize=200)
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        """Alustaa näkymän."""

        self._frame = ttk.Frame(master=self._root)

        self._initialize_subscription_title()
        row = 1
        for subscription in self._subscriptions:
            self._initialize_subscription(subscription,row)
            row += 1

class CreateApplicationView:
    """Tilausten listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root, show_login_view, show_create_subscription_view):
        """Luokan konstruktori, mikä luo uuden tilausnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            show_login_view:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä kirjautuu ulos.
            show_create_subscription_view:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä haluaa lisätä uuden tilauksen.
        """

        self._root = root
        self._show_login_view = show_login_view
        self._show_create_subscription_view = show_create_subscription_view
        self._frame = None
        self._user = subscription_service.return_current_user()
        self._subscription_frame = None
        self._subscription_view = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def _logout_handler(self):

        subscription_service.logout()
        self._show_login_view()

    def _handle_set_subscription_ending(self, subscription_id):
        subscription_service.set_subscription_ending(subscription_id)
        self._initialize_header()
        self._initialize_subscriptions()

    def _initialize_sum_of_subscriptions(self, sum):
        sum_of_subs = ttk.LabelFrame(master=self._frame, text="Total sum of you current subscriptions:")
        sum_str = '{:.2f}€'.format(sum)
        total_price = ttk.Label(master=sum_of_subs, text=sum_str)

        sum_of_subs.grid(row=2, column =0, padx=5, pady=5)
        total_price.grid(padx=5, pady=5)

    def _initialize_header(self):
        heading_label = ttk.Label(
            master=self._frame, text=f"Hello {self._user.username}!", font=("Arial", 14))

        heading_label.grid(row=0, column=0, sticky=constants.W, pady=5)

        subscriptions = subscription_service.get_subscriptions()
        if subscriptions:
            sum = subscription_service.get_sum_of_subscriptions(subscriptions)
        else:
            sum = 0.0

        self._initialize_sum_of_subscriptions(sum)

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)

        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)


    def _initialize_subscriptions(self):
        if self._subscription_view:
            self._subscription_view.destroy()

        subscriptions = subscription_service.get_subscriptions()

        if subscriptions:
            self._subscription_view = SubscriptionView(self._subscription_frame, subscriptions, self._handle_set_subscription_ending)
            self._subscription_view.pack()
        else:
            no_subscriptions_label= ttk.Label(master=self._subscription_frame,
                text="No active subscriptions", foreground="red", font=("Arial", 12))
            no_subscriptions_label.pack()

    def _initialize_footer(self):
        add_subscription_button = ttk.Button(master=self._frame, text="Add new Subscription",
            command=self._show_create_subscription_view)

        add_subscription_button.grid(row=5, column=1, padx=5, pady=5, sticky=constants.EW)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()

        self._subscription_frame = ttk.Frame(master=self._frame)
        self._initialize_subscriptions()

        self._subscription_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )


        self._initialize_footer()
