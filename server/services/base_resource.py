from flask_restful import Resource
from ..models.dbconn import db
from flask import make_response, request, abort

# CRUD
# Create     POST        /items
# Read       GET         /items  single resource /items/<id>
# Update     PATCH/PUT
# Delete     DELETE

class AllResource(Resource):

    def __init__(self, model, resource_name="Items"):
        super().__init__()
        self.Model = model
        self.resource_name = resource_name


    def get(self):
        # Pagination
        # query_parameter -> per_page
        # query_parameter -> page
        # /items?per_page=10&page=1
        per_page = int(request.args.get("per_page", 10))
        page = int(request.args.get("page", 1))

        query = self.Model.query.limit(per_page).offset( (page-1) * per_page )
        total_count = self.Model.query.count()

        categories_dict = [c.to_dict() for c in query.all()] # List comprehesion
        
        return make_response({ "data":categories_dict, "total": total_count}, 200)
    
    def post(self):

        item = self.Model()
        for field, value in request.json.items():
            setattr(item, field, value)

        db.session.add(item)
        db.session.commit()
        print(item)

        return make_response({"data": item.to_dict()}, 201)
    

class SingleResource(Resource):

    def __init__(self, model, resource_name="Items"):
        super().__init__()
        self.Model = model
        self.resource_name = resource_name

    def get(self, id):

        item = self.Model.query.filter_by(id=id).first()
        if item == None: # Page found
            abort(400, message=f"The {self.resource_name} with id {id} does not exist")

        return make_response({"data": item.to_dict()}, 200)
    
    def patch(self, id):

        item = self.Model.query.filter_by(id=id).first()
        if item == None: # Page found
            abort(400, message=f"The {self.resource_name} with id {id} does not exist")

        for field, value in request.json.items():
            if hasattr(item, field):
                setattr(item, field, value)

        db.session.commit()
        print(item)

        return make_response({"data": item.to_dict()}, 201)
