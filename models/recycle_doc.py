from mongoengine import Document


class RecycleDocument(Document):
    meta = {
        'abstract': True
    }
