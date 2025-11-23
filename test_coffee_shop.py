import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffeeShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_all = list(Order.all)

    @classmethod
    def tearDownClass(cls):
        # Restore the original list after all tests are done
        Order.all = cls.original_all

    def setUp(self):
        # Clear the list before each test to ensure isolation
        Order.all = []
        # Setup common objects for tests
        self.c1 = Customer("Tonny")
        self.c2 = Customer("Wangechi")
        self.cf1 = Coffee("Latte")
        self.cf2 = Coffee("Espresso")
        self.o1 = Order(self.c1, self.cf1, 5.0)
        self.o2 = Order(self.c1, self.cf1, 4.5)
        self.o3 = Order(self.c2, self.cf2, 3.0)
        self.o4 = Order(self.c2, self.cf1, 5.5)

    def test_order_creation_and_associations(self):
        """Test that Order initialization correctly sets attributes and associations."""
        self.assertEqual(len(Order.all), 4)
        self.assertIn(self.o1, Order.all)
        
        # Test Customer associations
        self.assertIn(self.o1, self.c1._orders)
        self.assertIn(self.o2, self.c1._orders)
        self.assertEqual(len(self.c1._orders), 2)

        # Test Coffee associations
        self.assertIn(self.o1, self.cf1._orders)
        self.assertIn(self.o2, self.cf1._orders)
        self.assertEqual(len(self.cf1._orders), 3) # cf1 has o1, o2, o4

    # --- Customer Tests ---   
    def test_customer_name_validation(self):
        """Test Customer name property validation."""
        # Valid name
        self.c1.name = "Charlie"
        self.assertEqual(self.c1.name, "Charlie")
        
        # Invalid name length (too short)
        with self.assertRaises(ValueError):
            self.c1.name = ""
            
        # Invalid name length (too long)
        with self.assertRaises(ValueError):
            self.c1.name = "ThisNameIsWayTooLong"

    def test_customer_coffees_method(self):
        """Test Customer.coffees() returns unique Coffee objects."""
        unique_coffees = self.c1.coffees()
        self.assertIsInstance(unique_coffees, list)
        self.assertEqual(len(unique_coffees), 2) # Latte and Espresso
        self.assertIn(self.cf1, unique_coffees)
        self.assertIn(self.cf2, unique_coffees)

    def test_customer_order_total_price(self):
        """Test Customer.order_total_price() calculates correct sum."""
        # Tonny's orders: 5.0 + 4.5 = 9.5
        self.assertAlmostEqual(self.c1.order_total_price(), 9.5)
        # Wangechi's orders: 3.0 + 5.5 = 8.5
        self.assertAlmostEqual(self.c2.order_total_price(), 8.5)

    def test_customer_most_aficionado(self):
        """Test Customer.most_aficionado() identifies the highest spender for a Coffee."""
        # Tonny spent 5.0 + 4.5 = 9.5 on Latte (cf1)
        # Wangechi spent 5.5 on Latte (cf1)
        self.assertEqual(Customer.most_aficionado(self.cf1), self.c1)

        # Only Wangechi ordered Espresso (cf2)
        self.assertEqual(Customer.most_aficionado(self.cf2), self.c2)
        
        # Test with no orders for a new coffee
        cf3 = Coffee("Mocha")
        self.assertIsNone(Customer.most_aficionado(cf3))

    # --- Coffee Tests ---
    def test_coffee_name_validation(self):
        """Test Coffee name property validation."""
        # Valid name
        self.cf1.name = "Cappuccino"
        self.assertEqual(self.cf1.name, "Cappuccino")
        
        # Invalid name length (too short)
        with self.assertRaises(ValueError):
            self.cf1.name = "No"

    def test_coffee_customer_method(self):
        """Test Coffee.customer() returns unique Customer objects."""
        # Latte (cf1) was ordered by Alice (o1, o2) and Wangechi (o4)
        unique_customers = self.cf1.customer()
        self.assertIsInstance(unique_customers, list)
        self.assertEqual(len(unique_customers), 2)
        self.assertIn(self.c1, unique_customers)
        self.assertIn(self.c2, unique_customers)

    def test_coffee_num_orders(self):
        """Test Coffee.num_orders() returns the total count."""
        self.assertEqual(self.cf1.num_orders(), 3)
        self.assertEqual(self.cf2.num_orders(), 1)
    
    def test_coffee_average_price(self):
        """Test Coffee.average_price() calculation."""
        # cf1 prices: 5.0, 4.5, 5.5. Sum = 15.0. Count = 3. Average = 5.0
        self.assertAlmostEqual(self.cf1.average_price(), 5.0)
        
        # cf2 prices: 3.0. Sum = 3.0. Count = 1. Average = 3.0
        self.assertAlmostEqual(self.cf2.average_price(), 3.0)
        
        # Test zero orders
        cf_new = Coffee("Drip")
        self.assertEqual(cf_new.average_price(), 0)

    # --- Order Tests ---
    def test_order_price_validation(self):
        """Test Order price property validation."""
        # Valid price
        self.o1.price = 7.5
        self.assertAlmostEqual(self.o1.price, 7.5)
        
        # Invalid price (too low)
        with self.assertRaises(ValueError):
            self.o1.price = 1.0
            
        # Invalid price (too high)
        with self.assertRaises(ValueError):
            self.o1.price = 10.1
            
        # Invalid price (not float/number)
        with self.assertRaises(ValueError):
            self.o1.price = "Free"
            
    def test_order_customer_validation(self):
        """Test Order customer property validation."""
        with self.assertRaises(TypeError):
            self.o1.customer = "NotACustomer"

    def test_order_coffee_validation(self):
        """Test Order coffee property validation."""
        with self.assertRaises(TypeError):
            self.o1.coffee = "NotACoffee"

if __name__ == '__main__':
    unittest.main()