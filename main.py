from flask import Flask
from flask_cors import *

import routes.invoice
import routes.menus
import routes.upload

app = Flask(__name__, static_folder='static', static_url_path='/static')

CORS(app, resources=r'/*')

app.config['UPLOAD_FOLDER'] = 'upload/'

routes.menus.add_route(app)
routes.upload.add_route(app)
routes.invoice.add_route(app)

if __name__ == '__main__':
    app.run(debug=True)
