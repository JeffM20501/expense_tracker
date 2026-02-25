from .dbconn import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    serialize_rules=('-categories.user', '-expenses.user',)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    anonymous_key=db.Column(db.String, unique=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    categories=db.relationship("Category", back_populates='user')
    expenses=db.relationship('Expense', back_populates='user')