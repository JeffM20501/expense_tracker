from .dbconn import db
from sqlalchemy_serializer import SerializerMixin

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # user = db.relationship("User", back_populates="category")

    expenses = db.relationship("Expense", back_populates="category")

    serialize_rules = ("-expense.category", )

