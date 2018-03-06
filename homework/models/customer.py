from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    phone = StringField()
    job = StringField()
    contacted = StringField(
