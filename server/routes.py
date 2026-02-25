from flask import Blueprint
from flask_restful import Api
from .models import *
from .services.base_resource import *

api_pb = Blueprint("api_bp", __name__)
api_v1 = Api(api_pb, prefix="/api/v1")

api_v1.add_resource(
    AllResource,
    "/categories",
    endpoint="/categories",
    resource_class_args=(Category, "Category")
)

api_v1.add_resource(
    SingleResource,
    "/categories/<id>",
    endpoint="/categories/<id>",
    resource_class_args=(Category, "Category")
)

api_v1.add_resource(
    AllResource,
    "/expenses",
    endpoint="/expenses",
    resource_class_args=(Expense, "Expenses")
)

api_v1.add_resource(
    SingleResource,
    "/expenses/<id>",
    endpoint="/expenses/<id>",
    resource_class_args=(Expense, "Expense")
)

# -------- User ------


api_v1.add_resource(
    AllResource,
    "/users",
    endpoint="/users",
    resource_class_args=(User, "Users")
)

api_v1.add_resource(
    SingleResource,
    "/users/<id>",
    endpoint="/users/<id>",
    resource_class_args=(User, "User")
)