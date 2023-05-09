from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.geometry("900x900")
    window.title("Subscription Manager App")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
