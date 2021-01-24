import json

from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()


@app.route("/")
def home():
    foods = DB.get_all_foods()
    foods = json.dumps(foods)
    return render_template("home.html", foods=foods)


@app.route("/savefood", methods=['POST'])
def save_food():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get("description")
    DB.add_food(category,
                 date,
                 latitude,
                 longitude,
                 description)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clear_all()

    except Exception as e:
        print(e)

    return home()


if __name__ == '__main__':
    app.run(port=5000, debug=True)