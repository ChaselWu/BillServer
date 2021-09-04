import json
import os

from flask import request
from flask_cors import cross_origin
from werkzeug.utils import secure_filename


def add_route(app):
    base_url = '/upload'

    @app.route(base_url + '/img', methods=['GET', 'POST', 'OPTIONS'])
    @cross_origin()
    def post_img():
        if request.method == 'OPTIONS':
            pass
        if request.method == 'POST':
            f = request.files['file']
            f.save(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
