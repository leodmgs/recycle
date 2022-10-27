import bcrypt
import falcon

from ..models.user import User
from .. import settings


class AuthMiddleware:
    async def process_request(self, req, resp):
        token = req.get_header('Authorization')
        challenges = ['']

        if token is None:
            description = 'Please provide an auth token as part of the request.'
            raise falcon.HTTPUnauthorized(
                title='Auth token required',
                description=description,
                challenges=challenges,
                href='http://docs.example.com/auth',
            )

        if not self.validate(token):
            description = (
                'The provided auth token is not valid. '
                'Please request a new token and try again.'
            )
            raise falcon.HTTPUnauthorized(
                title='Authentication required',
                description=description,
                challenges=challenges,
                href='http://docs.example.com/auth',
            )

    def validate(self, token):
        prefix = 'Bearer '
        if not token.startswith(prefix):
            return False
        if token.replace(prefix, '') == 'bingo!':
            return True 
        else:
            return False        
