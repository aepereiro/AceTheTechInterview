import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Configuration for the number of entries
num_customers = 50
num_products = 30
num_orders = 100
num_order_details = 200

# File to store SQL commands
filename = 'populate_data.sql'

with open(filename, 'w') as file:
    # Populate Customers
    file.write("-- Populating Customers\n")
    for _ in range(num_customers):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        file.write(f"INSERT INTO Customer (FirstName, LastName, Email) VALUES ('{first_name}', '{last_name}', '{email}');\n")
    
    # Populate Products
    file.write("\n-- Populating Products\n")
    for _ in range(num_products):
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()
        price = round(random.uniform(5.00, 1000.00), 2)  # Random price between $5 and $1000
        file.write(f"INSERT INTO Product (ProductName, Price) VALUES ('{product_name}', {price});\n")
    
    # Populate PurchaseOrders
    file.write("\n-- Populating PurchaseOrders\n")
    for _ in range(num_orders):
        customer_id = random.randint(1, num_customers)
        order_date = fake.date_between(start_date='-2y', end_date='today').isoformat()
        file.write(f"INSERT INTO PurchaseOrder (CustomerID, OrderDate) VALUES ({customer_id}, '{order_date}');\n")
    
    # Populate OrderDetails
    file.write("\n-- Populating OrderDetails\n")
    for _ in range(num_order_details):
        order_id = random.randint(1, num_orders)
        product_id = random.randint(1, num_products)
        quantity = random.randint(1, 20)  # Quantity between 1 and 20
        file.write(f"INSERT INTO OrderDetail (OrderID, ProductID, Quantity) VALUES ({order_id}, {product_id}, {quantity});\n")

print(f"Data successfully written to {filename}")
