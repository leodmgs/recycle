import json
import logging

from ..models.event import Event


class CreateEvent:

    def __init__(self) -> None:
        self.logger = logging.getLogger('simpleExample')

    async def on_get(self, req, res):
        self.logger.debug(
            f"[CreateEvent] on_get params: {req.params.get('event_name')}")
        if 'id' in req.params:
            events_data = Event.get_by_id(req.params.get('id'))
        elif 'event_name' in req.params:
            events_data = Event.get_by_name(req.params.get('event_name'))
        else:
            events_data = Event.get_all()
        self.logger.debug(f'Events found: {events_data}')
        res.media = events_data

    async def on_post(self, req, res):
        data = await req.media
        event = Event(**data)
        event.save()
        event.reload()
        res.media = json.loads(event.to_json())
