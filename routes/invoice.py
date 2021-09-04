import base64
import os

import requests
from werkzeug.utils import secure_filename


def add_route(app):
    base_url = '/invoice'

    @app.route(base_url + '/<string:img_file>/', methods=['GET'])
    def get_info(img_file):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/invoice"
        # 二进制方式打开图片文件
        f = open(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], secure_filename(img_file)), 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        access_token = "24.6f4713f77119b932b3179973581183c4.2592000.1633346901.282335-24797943"
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json(), 200, {'ContentType': 'application/json'}
