import json
import logging

import falcon
import falcon.asgi


class SignUpEndpoint:
    async def on_post(self, req, resp):
        """Handles POST requests"""
        logging.info(req)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.text = json.dumps({'result': 'sign-up page'})


# falcon.asgi.App instances are callable ASGI apps...
# in larger applications the app is created in a separate file
app = falcon.asgi.App()
signup = SignUpEndpoint()
app.add_route('/signup', signup)
