from flask_restful import Resource
from ..models import Category
from ..models.dbconn import db
from flask import make_response, request, abort

# CRUD
# Create     POST        /categories
# Read       GET         /categories  single resource /categories/<id>
# Update     PATCH/PUT
# Delete     DELETE

class CategoriesResource(Resource):

    def get(self):
        # Pagination
        # query_parameter -> per_page
        # query_parameter -> page
        # /categories?per_page=10&page=1
        per_page = int(request.args.get("per_page", 10))
        page = int(request.args.get("page", 1))

        query = Category.query.limit(per_page).offset( (page-1) * per_page )
        total_count = Category.query.count()

        categories_dict = [c.to_dict() for c in query.all()] # List comprehesion
        
        return make_response({ "data":categories_dict, "total": total_count}, 200)
    
    def post(self):

        category = Category()
        for field, value in request.json.items():
            setattr(category, field, value)

        db.session.add(category)
        db.session.commit()
        print(category)

        return make_response({"data": category.to_dict()}, 201)
    

class CategoryResource(Resource):

    def get(self, id):

        category = Category.query.filter_by(id=id).first()
        if category == None: # Page found
            abort(400, message=f"The category with id {id} does not exist")

        return make_response({"data": category.to_dict()}, 200)
    
    def patch(self, id):

        category = Category.query.filter_by(id=id).first()
        if category == None: # Page found
            abort(400, message=f"The category with id {id} does not exist")

        for field, value in request.json.items():
            if hasattr(category, field):
                setattr(category, field, value)

        db.session.commit()
        print(category)

        return make_response({"data": category}, 201)
