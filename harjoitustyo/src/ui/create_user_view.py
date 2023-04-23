from tkinter import ttk, constants, StringVar
from services.subscription_service import subscription_service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._show_login_view = show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        self._frame.place(relx=0.5, rely=0.5, anchor='center')

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        try:
            subscription_service.create_user(username_value, password_value)
            self._show_message(f"User {username_value} created succesfully. Please wait.")
            self._root.after(3000, self._show_login_view)

        except UsernameExistsError:
            self._show_message(f"Username {username_value} already exists")

    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()

    def _initialize_username_and_password_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1, columnspan=3, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, pady=5)
        self._password_entry.grid(row=2, column=1, columnspan=3, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._message_variable = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame, textvariable=self._message_variable, foreground="green", font=("Arial", 14, "bold"))

        self._message_label.grid(row=5, column=1, pady=(10, 0))

        heading_label = ttk.Label(
            master=self._frame, text="Create user", font=("Arial", 13))
        heading_label.grid(row=0, column=1, sticky=constants.NSEW, pady=5)

        self._initialize_username_and_password_field()

        login_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_login_view)
        create_user_button = ttk.Button(
            master=self._frame, text="Create user", command=self._create_user_handler)

        login_button.grid(row=3, column=1, padx=5, pady=5)
        create_user_button.grid(row=3, column=2, padx=5, pady=5)
