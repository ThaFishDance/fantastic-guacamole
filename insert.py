import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("AZN_HDB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open('dishes.csv', 'r')
    reader = csv.reader(f)
    for name, price in reader:
        dish = Dish(name=name, price=price)
        db.session.add(dish)
        print(f'Added {name} to dishes with price: {price}')
    db.session.commit()
            

if __name__ == "__main__":
    with app.app_context():
        main()