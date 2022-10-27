import falcon.asgi

from .config import Config
from .endpoints.event import (EventCreateEndpoint, EventReadListEndpoint,
                              EventReadUpdateDeleteEndpoint)
from .endpoints.user import (UserCreateEndpoint, UserReadEventsEndpoint,
                             UserReadListEndpoint,
                             UserReadUpdateDeleteEndpoint)
from .middleware import auth, mongo


def create_app(config=None):
    config = config or Config()

    app = falcon.asgi.App(middleware=[auth.AuthMiddleware()])
    app.add_route('/events', EventReadListEndpoint())
    app.add_route('/event', EventCreateEndpoint())
    app.add_route('/event/{event_id}', EventReadUpdateDeleteEndpoint())

    app.add_route('/users', UserReadListEndpoint())
    app.add_route('/user', UserCreateEndpoint())
    app.add_route('/user/{user_id}', UserReadUpdateDeleteEndpoint())
    app.add_route('/user/{user_id}/events', UserReadEventsEndpoint())

    return app


mongo.setup()
