from flask import Flask, make_response, request
from dotenv import load_dotenv
from .models.dbconn import db
from .models import Category,User,Expense
from flask_migrate import Migrate
from flask_restful import Api, Resource,abort
from .services.category_resource import CategoriesResource, CategoryResource
from .services.user_resource import UsersResource
from .services.base_resource import AllResource, SingleResource

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
    
    api.add_resource(AllResource,
                    '/users',
                    endpoint='/users',
                    resource_class_args=(User, 'users'))
    
    api.add_resource(AllResource, 
                    '/categories', 
                    endpoint='/categories',
                    resource_class_args=(Category, 'categories'))
    api.add_resource(SingleResource,
                    '/category/<int:id>',
                    endpoint='/category/<int:id>',
                    resource_class_args=(Category, 'categories'))
    class Expenses(Resource):
        def get(self):
            expenses_dict=[e.to_dict() for e in Expense.query.all()]
            return make_response(expenses_dict,200)
    api.add_resource(Expenses,'/expenses')

    return app

