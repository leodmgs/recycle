import falcon.asgi

from .config import Config
from .endpoints.create_event import CreateEvent
from .middleware import mongo


def create_app(config=None):
    config = config or Config()

    app = falcon.asgi.App()
    app.add_route('/event', CreateEvent())

    return app


mongo.setup()
