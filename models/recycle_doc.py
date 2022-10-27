from typing import Union

from bson import ObjectId
from mongoengine import Document


class RecycleDocument(Document):
    meta = {
        'abstract': True
    }

    @classmethod
    def get_by_id(cls, id: Union[str, ObjectId]):
        if isinstance(id, str):
            id = ObjectId(id)
        queryset = cls.objects.get(id=id)
        return queryset.to_json()

    @classmethod
    def get_all(cls):
        queryset = cls.objects()
        return [q.to_json() for q in queryset]

    def to_json():
        not NotImplementedError()

    def __str__(self):
        self.to_json()
