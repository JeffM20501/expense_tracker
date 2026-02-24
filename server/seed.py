from .app import create_app
from .models.dbconn import db
from .models import Category

with create_app().app_context() as app:
    
    categories = [
        Category(name="Food"),
        Category(name="Rent"),
        Category(name="Health & Fitness"),
        Category(name="Entertainment"),
        Category(name="Transport"),
        Category(name="Airtime")
    ]

    db.session.add_all(categories)
    db.session.commit()