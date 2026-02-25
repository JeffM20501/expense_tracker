from flask import make_response
from flask_restful import Resource, abort
from ..models import User

class UsersResource(Resource):
    def get(self):
        users_dict=[u.to_dict() for u in User.query.all()]
        return make_response(users_dict,200)