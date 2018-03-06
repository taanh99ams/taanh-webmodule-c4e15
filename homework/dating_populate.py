import mlab
from models.dating import Dating
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
personality1 = ['vui vẻ', 'hòa đồng','yêu đời','hiền lành','năng động']
personality2 = ['chăm chỉ','ân cần','hài hước','dễ tính']
city = ['Hanoi','Danang', 'Ho Chi Minh','Hue','Hai Phong','Can Tho','Da Lat']

for i in range(50):
    dating = Dating(name=fake.name(),
                    yob=randint(1990,1999),
                    phone=fake.phone_number(),
                    address=choice(city),
                    description=choice(personality1) + " và " + choice(personality2),
                    measurement=[randint(70,100), randint(50,70), randint(70,100)],
                    image='http://bit.ly/web3girl{0}'.format(randint(0,9)))
    print('Populating data', i+1)
    dating.save()




# name = StringField()
# yob = IntField()
# phone = IntField()
# address = StringField()
# description = StringField()
# measurement = StringField()
