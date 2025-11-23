#  Coffee Shop Association Project

This is a simple Python project demonstrating **Object-Relational Mapping (ORM)** concepts using standard Python classes. It models a simple coffee shop domain with three main classes: `Customer`, `Coffee`, and `Order`.

The core feature is the association of these objects, allowing you to track which customers ordered which coffees and calculate related metrics (e.g., total spending, average price).
##  Installation and Setup

This project uses standard Python and has no external dependencies beyond the three included files.

1.  **Clone the repository (if applicable) or save the files:**
    Ensure you have the following three files in the same directory:
    * `customer.py`
    * `coffee.py`
    * `order.py`

2.  **Ensure Python is installed:**
    This code is compatible with Python 3.

## Usage

The classes are designed to be used interactively or as part of a larger application.

### 1. Creating Objects and Orders

You must create `Customer` and `Coffee` instances before creating an `Order`.

```python
from customer import Customer
from coffee import Coffee
from order import Order

# 1. Create Customers and Coffees
Tonny = Customer("Tonny")
Wangechi = Customer("Wangechi")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# 2. Make Orders (This automatically associates the objects)
# Syntax: Order(customer_instance, coffee_instance, price)

order1 = Order(Tonny, latte, 5.0)
order2 = Order(Wangechi, espresso, 4.0)
order3 = Order(Tonny, latte, 5.5)

