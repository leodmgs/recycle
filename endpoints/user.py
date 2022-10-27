import logging

from mongoengine.errors import NotUniqueError, ValidationError

from ..logger import set_up_logging

logger = set_up_logging()

from ..models.event import Event
from ..models.user import User


class UserReadListEndpoint:
    async def on_get(self, req, res):
        query_result = User.get_all()
        res.media = query_result


class UserCreateEndpoint:
    async def on_post(self, req, res):
        media = await req.media
        user = User(**media)
        try:
            user.save()
        except NotUniqueError:
            res.media = {"status": "error", "details": f"user {media['email']} already exists"}
            return
        except ValidationError as err:
            res.media = {"status": "error", "details": err.to_dict()}
            return
        user.reload()
        res.media = user.to_json()


class UserReadUpdateDeleteEndpoint:
    async def on_get(self, req, res, **kwargs):
        query_result = {}
        if 'user_id' in kwargs:
            query_result = User.get_by_id(kwargs["user_id"])
        res.media = query_result

    async def on_patch(self, req, res, **kwargs):
        user = User.objects.get(id=kwargs["user_id"])
        media = await req.media
        user.update(**media)
        user.reload()
        res.media = {"status": "success"}

    async def on_delete(self, req, res, **kwargs):
        user = User.objects.get(id=kwargs["user_id"])
        user.delete()
        res.media = {"status": "success"}


class UserReadEventsEndpoint:
    async def on_get(self, req, res, **kwargs):
        events = []
        if 'user_id' in kwargs:
            query_result = Event.objects(user_id=kwargs["user_id"])
            events = [e.to_json() for e in query_result]
        res.media = events
