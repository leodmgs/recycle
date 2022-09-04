import datetime
import json
import pytz
from bson import ObjectId
from typing import Union

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

    @classmethod
    def get_by_id(cls, id: Union[str, ObjectId]):
        if not id:
            raise ValueError('invalid id argument')
        if isinstance(id, str):
            id = ObjectId(id)
        queryset = cls.objects(id=id)
        return json.loads(queryset.to_json())

    @classmethod
    def get_by_name(cls, event_name: str):
        if not event_name:
            raise ValueError('invalid event_name argument')
        queryset = cls.objects(name=event_name)
        return json.loads(queryset.to_json())

    @classmethod
    def get_all(cls):
        queryset = cls.objects()
        return json.loads(queryset.to_json())
