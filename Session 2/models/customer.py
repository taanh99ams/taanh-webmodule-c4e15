from mongoengine import Document, StringField, IntField, BooleanField

class Customer(Document):
    name = StringField()
    gender = IntField()
    phone = StringField()
    job = StringField()
    contacted = StringField()
