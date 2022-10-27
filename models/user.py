import datetime

import bcrypt
import pytz
from mongoengine import DateTimeField, StringField

from .. import settings
from .recycle_doc import RecycleDocument


class User(RecycleDocument):

    meta = {
        'collection': 'users'
    }

    first_name = StringField(min_length=3, max_length=32, required=True)
    last_name = StringField(min_length=3, max_length=32, required=True)
    password = StringField(required=True)
    email = StringField(min_length=8, max_length=64, required=True, unique=True)
    phone = StringField(min_length=10, max_length=12, required=True)
    created_at = DateTimeField(required=True)

    def clean(self):
        _password_digest = bcrypt.hashpw(
            self.password.encode("utf-8"),
            settings.SECRET_KEY_BASE.encode("utf-8"))
        self.password = _password_digest.decode("utf-8")
        self.created_at = datetime.datetime.now(pytz.UTC)

    def to_json(self):
        return {
            "id": str(self.pk),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at.strftime("%c"),
        }
