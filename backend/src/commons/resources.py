import json

from flask import make_response
from flask_restful import Resource
from plotly.utils import PlotlyJSONEncoder


def output_chart_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = json.dumps(data, cls=PlotlyJSONEncoder) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


class PlotlyChartResource(Resource):
    representations = {
        'application/json': output_chart_json
    }
