from flask import request, make_response
from flask_restful import Resource,abort
from ..models import Category
from ..models.dbconn import db

class CategoriesResource(Resource):
    def get(self):
        per_page=request.args.get("per_page",10)
        page=request.args.get("page", 1)
        
        query=Category.query.limit(per_page).offset((page-1)*per_page)
        total_count=Category.query.count()
        categories_dict=[c.to_dict() for c in query.all()]
        
        return make_response({"data":categories_dict,"total":total_count}, 200)
    
    def post(self):
        category=Category()
        for field,value in request.json.items():
            setattr(category,field,value)
        
        db.session.add(category)
        db.session.commit()
        
        return make_response({'data':category}, 201)

class CategoryResource(Resource):
    def get(self,id):
        category=Category.query.filter_by(id=id).first()
        if category==None:
            abort(404, message=f'The Category with id {id} does not exist')
        return make_response({"data":category.to_dict()}, 200)
    
    def post(self,id):
        category=Category.query.filter_by(id=id).first()
        if category==None:
            abort(404, message=f'The Category with id {id} does not exist')
        for field,value in request.json.items():
            if hasattr(category,field):
                setattr(category,field,value)
        
        db.session.commit()
        
        return make_response({'data':category}, 201)