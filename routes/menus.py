import json

import requests
from flask import jsonify


def add_route(app):
    base_url = '/menus'

    @app.route(base_url + '/<string:name>/', methods=['GET'])
    def get_menu(name):
        r = requests.get('http://127.0.0.1:5000/static/menus/' + name + '.json').text
        return jsonify(json.loads(r))
