from order import Order
from coffee import Coffee


class Customer:
    def ___init___(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val
        else:
            raise ValueError("Name must be between 1 and 15 characters")

    def orders(self):
        return self.orders

    def coffees(self):
        # return a list of all coffee orders a customer has made
        return list({order.coffee for order in self._orders})

    # Define new order instance that associates it with this customer
    def make_order(self, coffee, price):
        return Order(self, coffee, price)

    def order_total_price(self):
        # Returns the total price spent by this customer across all their orders.
        return sum(order.price for order in self._orders)

    @classmethod
    def most_aficionado(coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be a Coffee instance.")
        # Filter orders for the specific coffee
        coffee_orders = [order for order in Order.all if order.coffee is coffee]
        if not coffee_orders:
            return None
        # Group orders by customer and calculate total spent on this coffee
        customer_spending = {}
        for order in coffee_orders:
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        most_spent_customer = max(customer_spending.items(), key=lambda item: item[1])[0]

        return most_spent_customer





