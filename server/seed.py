#!/usr/bin/env python3

from app import app
from models import db, Customer, Review, Item

def seed_data():
    with app.app_context():
        # Clear existing data
        try:
            Customer.query.delete()
            Review.query.delete()
            Item.query.delete()
            db.session.commit()  # Commit deletions

            # Seed customers
            customer1 = Customer(name='Tal Yuri')
            customer2 = Customer(name='Raha Rosario')
            customer3 = Customer(name='Luca Mahan')
            db.session.add_all([customer1, customer2, customer3])
            db.session.commit()

            # Seed items
            item1 = Item(name='Laptop Backpack', price=49.99)
            item2 = Item(name='Insulated Coffee Mug', price=9.99)
            item3 = Item(name='6 Foot HDMI Cable', price=12.99)
            db.session.add_all([item1, item2, item3])
            db.session.commit()

            # Seed reviews
            db.session.add(Review(comment="zipper broke the first week",
                                   customer=customer1, item=item1))
            db.session.add(Review(comment="love this backpack!",
                                   customer=customer2, item=item1))
            db.session.add(Review(comment="coffee stays hot for hours!",
                                   customer=customer1, item=item2))
            db.session.add(Review(comment="best coffee mug ever!",
                                   customer=customer3, item=item2))
            db.session.add(Review(comment="cable too short",
                                   customer=customer3, item=item3))
            db.session.commit()

            print("Database seeded successfully!")

        except Exception as e:
            db.session.rollback()  # Roll back on error
            print(f"Error seeding data: {e}")

if __name__ == '__main__':
    seed_data()
