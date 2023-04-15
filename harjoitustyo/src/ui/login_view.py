from tkinter import Tk, ttk, constants, StringVar


class LoginView:
    def __init__(self, root, handle_create_user_view):
        self._root = root
        self._handle_create_user_view = handle_create_user_view
        self._frame = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        self._frame.place(relx=0.5, rely=0.5, anchor='center')

    def destroy(self):
        self._frame.destroy()

    def _initialize_username_and_password_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, columnspan=3, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, pady=5)
        password_entry.grid(row=2, column=1, columnspan=3, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._message_variable = StringVar(self._frame)
        self._message_label = ttk.Label(
            master=self._frame, textvariable=self._message_variable)
        self._message_label.grid(pady=5)

        heading_label = ttk.Label(
            master=self._frame, text="Login or create a user", font=("Arial", 13))
        heading_label.grid(row=0, column=1, columnspan=3,
                           sticky=constants.NSEW, pady=5)

        self._initialize_username_and_password_field()

        login_button = ttk.Button(master=self._frame, text="Login")
        create_user_button = ttk.Button(
            master=self._frame, text="Create user", command=self._handle_create_user_view)

        login_button.grid(row=3, column=1, padx=5, pady=5)
        create_user_button.grid(row=3, column=3, padx=5, pady=5)