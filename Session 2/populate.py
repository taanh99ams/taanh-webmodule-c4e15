import mlab
from models.service import Service
from faker import Faker
from random import randint, choice

mlab.connect()

faker = Faker()
# service = Service(name='Adney',
#                     yob="1997",
#                     gender=1,
#                     height=170,
#                     phone="0981641654",
#                     address="Hanoi",
#                     status=True)
#
# service.save()
# print(faker.phone_number())

for i in range(50):
    print('Saving service', i+1, '.....')
    service = Service(name=faker.name(),
                        yob=randint(1990, 2000),
                        gender=choice(['Male','Female']),
                        height=randint(150, 175),
                        phone=faker.phone_number(),
                        address=faker.address(),
                        status=choice([True, False]))

    service.save()
