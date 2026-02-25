from .app import create_app
from .models.dbconn import db
from .models import Category, User,Expense
from faker import Faker
import random

with create_app().app_context():
    
    db.session.query(Expense).delete()
    db.session.query(Category).delete()
    db.session.query(User).delete()
    db.session.commit()
    print('✅Dropped existing tables')
    fake=Faker()
    
    users=[]
    for _ in range(10):
        try:
            user=User(
                email=fake.unique.email(),
                name=fake.unique.first_name(),
                anonymous_key=fake.unique.random_int()
            )
            if user:
                users.append(user)
        except Exception as e:
            print(f'❌ Falied to create user: {e}')
    db.session.add_all(users)
    db.session.commit()
    print('✅ Users Created')
    
    categories_list=['Food','Rent','Health & Fitness', 'Enterainment', 'Transport', 'Airtime']
    categories = []
    try:
        for name in categories_list:
            new_cat=Category(
                name=name,
                description=fake.sentence(),
                user_id=random.choice(users).id if users else None
            )
            if new_cat:
                categories.append(new_cat)
    except Exception as e:
        print(f'❌ Error when creatin Categories: {e}')
    
    db.session.add_all(categories)
    db.session.commit()
    print('✅Categories Created')
    
    expenses=[]
    
    for _ in range(10):
        try:
            new_expense=Expense(
                amount=round(random.uniform(500, 20000),2), 
                description=fake.sentence(),
                user_id=random.choice(users).id if users else None,
                category_id =random.choice(categories).id if users else None
            )
            expenses.append(new_expense)
        except Exception as e:
            print(f'❌ Failed to create Expense: {e}')
    db.session.add_all(expenses)
    db.session.commit()
    
    print('✅ Expenses created')
