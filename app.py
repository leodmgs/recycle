import falcon.asgi

from .config import Config
from .endpoints.create_event import CreateEventEndpoint
from .endpoints.user import UserEndpoint
from .middleware import mongo


def create_app(config=None):
    config = config or Config()

    app = falcon.asgi.App()
    app.add_route('/event', CreateEventEndpoint())
    app.add_route('/user', UserEndpoint())

    return app


mongo.setup()
