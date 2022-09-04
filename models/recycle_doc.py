import json
from bson import ObjectId
from typing import Union

from mongoengine import Document


class RecycleDocument(Document):
    meta = {
        'abstract': True
    }

    @classmethod
    def get_by_id(cls, id: Union[str, ObjectId]):
        if not id:
            raise ValueError('invalid id argument')
        if isinstance(id, str):
            id = ObjectId(id)
        queryset = cls.objects(id=id)
        return json.loads(queryset.to_json())

    @classmethod
    def get_by_name(cls, name: str):
        if not name:
            raise ValueError('invalid name argument')
        queryset = cls.objects(name=name)
        return json.loads(queryset.to_json())

    @classmethod
    def get_all(cls):
        queryset = cls.objects()
        return json.loads(queryset.to_json())
