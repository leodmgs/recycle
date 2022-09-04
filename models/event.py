import datetime
import json
import pytz

from mongoengine import DateTimeField, StringField
from mongoengine import ValidationError
from .recycle_doc import RecycleDocument


class Event(RecycleDocument):

    meta = {
        'collection': 'events'
    }
    name = StringField(min_length=3, max_length=128, required=True)
    target_date = DateTimeField(required=True)
    created_at = DateTimeField(required=True)

    def clean(self):
        self.created_at = datetime.datetime.now(pytz.UTC)
        if not isinstance(self.target_date, str):
            ValidationError('target_date must be str')
        parsed_date = datetime.datetime.strptime(self.target_date, '%m%d%Y')
        self.target_date = parsed_date
