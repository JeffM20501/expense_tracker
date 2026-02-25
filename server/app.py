from flask import Flask, make_response
from dotenv import load_dotenv
from .models.dbconn import db
from .models import Category,User,Expense
from flask_migrate import Migrate
from flask_restful import Api, Resource

load_dotenv()

def create_app():
    app = Flask(__name__)
    api=Api(app)
    app.config.from_prefixed_env()

    Migrate(app, db)

    db.init_app(app)

    class Index(Resource):
        def get(self):
            resopnse_body={"message": "Expenses DB"}
            return make_response(resopnse_body, 200)
        
    api.add_resource(Index, '/')
    
    class Users(Resource):
        def get(self):
            users_dict=[u.to_dict() for u in User.query.all()]
            return make_response(users_dict,200)
    
    api.add_resource(Users,'/users')
    class Categories(Resource):
        def get(self):
            categories_dict=[c.to_dict() for c in Category.query.all()]
            
            return make_response(categories_dict, 200)
        
    api.add_resource(Categories, '/categories')
    
    class Expenses(Resource):
        def get(self):
            expenses_dict=[e.to_dict() for e in Expense.query.all()]
            return make_response(expenses_dict,200)
    api.add_resource(Expenses,'/expenses')

    return app

