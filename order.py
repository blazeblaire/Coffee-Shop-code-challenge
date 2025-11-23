# from customer import Customer
# from coffee import Coffee

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # Add the new Order instance to the class-level list
        Order.all.append(self)
        # Add this order to the related customer's and coffee's internal lists
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def price(self):
        return self.price
    @price.setter
    def price(self, val):
        if isinstance(val, float) and 1.0 < val <10.0:
            self._price = val
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")

    @property
    def customer(self):
        return self.customer
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            TypeError("Customer must be an instance of the coffee class")

    @property
    def coffee(self):
        return self.coffee
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            TypeError("Coffee must be an instance of the coffee class")

    @classmethod
    def all_orders(cls):
        return cls.all
