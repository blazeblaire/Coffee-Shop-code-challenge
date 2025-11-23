# from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and len(val) >= 3:
            self._name = val
        else:
            raise ValueError("Name must be at least three characters")


    def orders(self):
        return self._orders

    """Returns a list of all unique Customer objects who have ordered this coffee.
        """
    def customer(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        """Returns the total number of times this coffee has been ordered"""
        return len(self._orders)
    def average_price(self):
        """Returns the average price for a coffee based on its orders."""
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)