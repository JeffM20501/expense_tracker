from flask import request, make_response
from flask_restful import Resource,abort
from ..models.dbconn import db

class AllResource(Resource):
    def __init__(self,model, resource_name='Items'):
        super().__init__()
        self.model=model
        self.resource_name=resource_name
        
    def get(self):
        per_page=request.args.get("per_page",10)
        page=request.args.get("page", 1)
        
        query=self.model.query.limit(per_page).offset((page-1)*per_page)
        total_count=self.model.query.count()
        models_dict=[c.to_dict() for c in query.all()]
        
        return make_response({"data":models_dict,"total":total_count}, 200)
    
    def post(self):
        model=self.model()
        for field,value in request.json.items():
            setattr(model,field,value)
        
        db.session.add(self.model)
        db.session.commit()
        
        return make_response({'data':self.model}, 201)

class SingleResource(Resource):
    def __init__(self,model, resource_name='Items'):
        super().__init__()
        self.model=model
        self.resource_name=resource_name
        
    def get(self,id):
        self.model=self.model.query.filter_by(id=id).first()
        if self.model==None:
            abort(404, message=f'The {self.resource_name} with id {id} does not exist')
        return make_response({"data":self.model.to_dict()}, 200)
    
    def post(self,id):
        self.model=self.model.query.filter_by(id=id).first()
        if self.model==None:
            abort(404, message=f'The self.model with id {id} does not exist')
        for field,value in request.json.items():
            if hasattr(self.model,field):
                setattr(self.model,field,value)
        
        db.session.commit()
        
        return make_response({'data':self.model}, 201)