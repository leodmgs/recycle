import json
import logging

from ..models.user import User


class UserEndpoint:

    def __init__(self) -> None:
        self.logger = logging.getLogger('simpleExample')

    async def on_get(self, req, res):
        self.logger.debug(f"[UserEndpoint] on_get params: {req.params}")
        if 'id' in req.params:
            user_data = User.get_by_id(id=req.params.get('id'))
        elif 'name' in req.params:
            user_data = User.get_by_name(name=req.params.get('name'))
        else:
            user_data = User.get_all()
        res.media = user_data

    async def on_post(self, req, res):
        media = await req.media
        self.logger.debug(f"[UserEndpoint] on_post media: {media}")
        user = User(**media)
        user.save()
        user.reload()
        res.media = json.loads(user.to_json())

