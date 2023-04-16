from tkinter import ttk, constants
from services.subscription_service import subscription_service

class CreateApplicationView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._show_login_view = show_login_view
        self.__frame = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Application view", font=("Arial", 13))

        heading_label.grid(row=0, column=1, sticky=constants.NSEW, pady=5)

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._show_login_view)

        logout_button.grid(row=3, column=1, padx=5, pady=5)
