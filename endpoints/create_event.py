import json
import logging

from ..models.event import Event


class CreateEventEndpoint:

    def __init__(self) -> None:
        self.logger = logging.getLogger('simpleExample')

    async def on_get(self, req, res):
        self.logger.debug(f"[CreateEventEndpoint] on_get params: {req.params}")
        if 'id' in req.params:
            events_data = Event.get_by_id(req.params.get('id'))
        elif 'event_name' in req.params:
            events_data = Event.get_by_name(req.params.get('event_name'))
        else:
            events_data = Event.get_all()
        self.logger.debug(f'Events found: {events_data}')
        res.media = events_data

    async def on_post(self, req, res):
        media = await req.media
        self.logger.debug(f"[CreateEventEndpoint] on_post media: {media}")
        event = Event(**media)
        event.save()
        event.reload()
        res.media = json.loads(event.to_json())
