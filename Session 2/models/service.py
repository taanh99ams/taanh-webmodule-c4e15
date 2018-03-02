from mongoengine import Document, StringField, IntField, BooleanField

class Service(Document):          #Service is just a name of my collection
    name = StringField()
    yob = IntField()
    gender = IntField() #0: male, 1: female
    height = IntField()
    phone = StringField()
    address = StringField()
    status = StringField()
