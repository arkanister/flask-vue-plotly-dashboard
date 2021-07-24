from flask_restful import Api as RestAPI

from api.healthcheck.resources import HealthyCheckResource
from api import reports


class API(RestAPI):

    def init_app(self, app):
        super().init_app(app)
        app.after_request(self.add_cors_headers)

    @staticmethod
    def add_cors_headers(response):
        """
        Enable support for CORS Headers.
        """
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response


api = API()

# Charts
api.add_resource(
    reports.GenresByUserScoreAVGChartResource,
    '/genres-by-user-score-avg')

api.add_resource(
    reports.PlatformsByUserScoreAVGChartResource,
    '/platforms-by-user-score-avg')

api.add_resource(
    reports.GameReleasePercentByPlatformInTheYearsChartResource,
    '/game-release-percent-by-platform-in-the-years')

# Infra
api.add_resource(HealthyCheckResource, '/healthy')
