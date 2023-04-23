from tkinter import ttk, constants
from datetime import datetime
from services.subscription_service import subscription_service

class SubscriptionView:
    def __init__(self, root, subscriptions):
        self._root = root
        self._subscriptions = subscriptions
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_subscription(self, subscription):
        item_frame = ttk.Frame(master=self._frame)

        name_label = ttk.Label(master=item_frame, text=subscription.name)
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        price_label = ttk.Label(master=item_frame, text="{:.2f}€".format(float(subscription.price)).replace('.', ','))
        price_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

        end_date = datetime.strptime(subscription.end_date, '%Y-%m-%d %H:%M:%S')
        end_date_label = ttk.Label(master=item_frame, text=end_date.strftime('%d-%m-%Y'))
        end_date_label.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for subscription in self._subscriptions:
            self._initialize_subscription(subscription)

class CreateApplicationView:
    def __init__(self, root, show_login_view, show_create_subscription_view):
        self._root = root
        self._show_login_view = show_login_view
        self._show_create_subscription_view = show_create_subscription_view
        self._frame = None
        self._user = subscription_service.return_current_user()
        self._subscription_frame = None
        self._subscription_view = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        subscription_service.logout()
        self._show_login_view()

    def _initialize_header(self):
        heading_label = ttk.Label(
            master=self._frame, text=f"Hello {self._user.username}!", font=("Arial", 14))

        heading_label.grid(row=0, column=0, sticky=constants.W, pady=5)
 
        separator = ttk.Separator(self._frame, orient='horizontal')
        separator.grid(row=1, column=0, columnspan=2, pady=10, sticky=constants.EW)

        user_label = ttk.Label(master=self._frame, text="Your active subscriptions:",
            font=("Arial", 13))

        user_label.grid(row=2, column=0, sticky=constants.EW)


    def _initialize_subscriptions(self):
        subscriptions = subscription_service.get_subscriptions()

        if subscriptions:
            self._subscription_view = SubscriptionView(self._subscription_frame, subscriptions)
            self._subscription_view.pack()
        else:
            no_subscriptions_label= ttk.Label(master=self._subscription_frame,
                text="No active subscriptions", foreground="red", font=("Arial", 12))
            no_subscriptions_label.pack()

    def _initialize_footer(self):

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)

        logout_button.grid(row=5, column=0, padx=5, pady=5, sticky=constants.EW)


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
