import datetime
import uuid


class Event:
    
    def __init__(self, name, date) -> None:
        self.name = name
        self.date = date
        self.created_at = datetime.datetime.now()
        self.id = uuid.uuid4()

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'date': self.date,
            'created_at': datetime.datetime.strftime(self.created_at, '%m-%d-%Y'),
        }
