from mongoengine import *

class Dating(Document):
    name = StringField()
    yob = IntField()
    phone = StringField()
    address = StringField()
    description = StringField()
    measurement = ListField()
    image = StringField()
