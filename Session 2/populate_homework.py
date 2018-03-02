import mlab
from models.customer import Customer
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(50):
    print('Populating customer data', i + 1)
    customer = Customer(name=fake.name(),
                        gender=randint(0,1),
                        phone=fake.phone_number(),
                        job=fake.job(),
                        contacted=choice(['contacted', 'not yet contacted'])
                        )
    customer.save()
