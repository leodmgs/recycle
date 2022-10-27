import json
import logging
from asyncio import events

from ..logger import set_up_logging

logger = set_up_logging()

from ..models.event import Event
from ..models.user import User


class EventReadListEndpoint:
    async def on_get(self, req, res):
        query_result = Event.get_all()
        res.media = query_result


class EventCreateEndpoint:
    async def on_post(self, req, res):
        media = await req.media
        event = Event(**media)
        user = User.get_by_id(media["user_id"])
        if not user:
            res.media = {"status": "error", "details": "User not found"}
        else:
            event.save()
            event.reload()
            res.media = event.to_json()


class EventReadUpdateDeleteEndpoint:
    async def on_get(self, req, res, *args, **kwargs):
        query_result = {}
        if 'event_id' in kwargs:
            query_result = Event.get_by_id(kwargs["event_id"])
        res.media = query_result

    async def on_patch(self, req, res, **kwargs):
        event = Event.objects.get(id=kwargs["event_id"])
        media = await req.media
        event.update(**media)
        event.reload()
        res.media = {"status": "success"}

    async def on_delete(self, req, res, **kwargs):
        event = Event.objects.get(id=kwargs["event_id"])
        event.delete()
        res.media = {"status": "success"}
