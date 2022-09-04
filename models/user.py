import datetime
import pytz

from mongoengine import DateTimeField, StringField
from .recycle_doc import RecycleDocument


class User(RecycleDocument):

    meta = {
        'collection': 'users'
    }
    name = StringField(min_length=3, max_length=128, required=True)
    email = StringField(min_length=8, max_length=64, required=True)
    phone = StringField(min_length=10, max_length=12, required=True)
    created_at = DateTimeField(required=True)

    def clean(self):
        self.created_at = datetime.datetime.now(pytz.UTC)
