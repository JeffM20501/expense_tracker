from .dbconn import db
from sqlalchemy_serializer import SerializerMixin

class Expense(db.Model, SerializerMixin):
    __tablename__ = "expenses"
    serialize_rules = ("-category.expenses", '-user.expenses')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    amount = db.Column(db.Double, nullable=False)
    description = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="expenses")

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="expenses")
