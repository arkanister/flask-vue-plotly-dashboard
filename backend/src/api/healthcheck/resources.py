from flask_restful import Resource
from werkzeug import Response


class HealthyCheckResource(Resource):

    def get(self):
        return Response('OK', content_type='text/plain')
