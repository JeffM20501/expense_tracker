from flask import Flask, make_response, request
from dotenv import load_dotenv
from .models.dbconn import db
from .models import Category,User,Expense
from flask_migrate import Migrate

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    Migrate(app, db)
    db.init_app(app)

    return app

