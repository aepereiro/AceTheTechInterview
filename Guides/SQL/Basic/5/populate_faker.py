import random
from faker import Faker
fake = Faker()

num_entries = 50
carriers = ['FedEx', 'UPS', 'DHL', 'USPS', 'Royal Mail']

filename = 'populate_shipping_info.sql'

with open(filename, 'w') as file:
    file.write("-- Populate ShippingInfo\n")
    for order_id in range(1, num_entries + 1):
        if random.choice([True, False]):
            shipped_date = fake.date_between(start_date='-1y', end_date='today')
            carrier = random.choice(carriers)
            file.write(f"INSERT INTO ShippingInfo (OrderID, ShippedDate, Carrier) VALUES ({order_id}, '{shipped_date}', '{carrier}');\n")

print(f"Data successfully written to {filename}")
