from flask import Flask
from dotenv import load_dotenv
from .models.dbconn import db
from .models import *
from flask_migrate import Migrate

from .routes import api_pb

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_pb)
    app.config.from_prefixed_env()

    Migrate(app, db)
    db.init_app(app)

    # api.add_resource(CategoriesResource, "/categories")
    # api.add_resource(CategoryResource, "/categories/<id>")

    return app