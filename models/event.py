import datetime

import pytz
from mongoengine import (DateTimeField, ReferenceField, StringField,
                         ValidationError)

from .recycle_doc import RecycleDocument


class Event(RecycleDocument):

    meta = {
        'collection': 'events'
    }

    user_id = ReferenceField('User', db_field='user_id', required=True)
    name = StringField(min_length=3, max_length=128, required=True)
    target_date = DateTimeField(required=True)
    created_at = DateTimeField(required=True)

    def clean(self):
        self.created_at = datetime.datetime.now(pytz.UTC)
        if not isinstance(self.target_date, str):
            ValidationError('target_date must be str')
        parsed_date = datetime.datetime.strptime(self.target_date, '%m%d%Y')
        self.target_date = parsed_date

    def to_json(self):
        return {
            "id": str(self.pk),
            'name': self.name,
            'target_date': self.target_date.strftime("%c"),
            'created_at': self.created_at.strftime("%c"),
        }
