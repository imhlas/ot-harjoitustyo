class Subscription:
    """Luokka, joka kuvaa yksittäistä tilausta

    Attributes:
        user_id: Tilaukselle kuuluvan käyttäjän tunniste.
        name: Tilauksen nimi.
        price: Tilauksen hinta.
        end_date: Tilauksen päättymispäivä.
    """
    def __init__(self, user_id, name, price, end_date):
        """Luokan konstruktori, joka luo uuden tilauksen.

        Args:
            user_id: Tilaukselle kuuluvan käyttäjän tunniste.
            name: Tilauksen nimi.
            price: Tilauksen hinta
            end_date: Tilauksen päättymispäivä
        """

        self.user_id = user_id
        self.name = name
        self.price = price
        self.end_date = end_date
