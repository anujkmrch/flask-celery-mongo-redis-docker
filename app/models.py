from mongoengine import Document, StringField, EmailField, IntField, ReferenceField


class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)


class Consent(Document):
    name = StringField(required=True)
    dob = StringField

class DataInsight(Document):
    clicks = IntField(required=True)
    consent = ReferenceField(Consent)
