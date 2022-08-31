import json
from typing import List, Union

from ..exceptions import AlreadyExistError
from ..models.event import Event


class CreateEvent:
    
    def __init__(self) -> None:
        self.events = []

    async def on_get(self, req, res):
        data = [e.to_dict() for e in self.events]
        print(data)
        res.media = data

    async def on_post(self, req, res):
        data = await req.media
        event = Event(**data)
        self.events.append(event)
        res.media = {'success': True}

    def get_events(self) -> List[Event]:
        return self.events

    def create_event(self, event: Event) -> Union[Event, None]:
        for e in self.events:
            if event.id == e.id:
                raise AlreadyExistError(f'Event with ID {event.id} already exists')
        self.events.append(event)
        return event
