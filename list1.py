import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("AZN_HDB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/')
def main():
    dishes = Dish.query.all() #returns a list
    # for dish in dishes:
    #     print(f'{dish.name} costs ${displayDishPrice(dish.price)}')
    return render_template('index.html', dishes=dishes)

# def displayDishPrice(number):
#     return number / 100

app.route

if __name__ == "__main__":
    with app.app_context():
        main()