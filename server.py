#!/usr/bin/env python3
from flask import Flask, abort, request, render_template
from data import data
import json
from flask_cors import CORS
from config import db, parse_json

app = Flask(__name__)
CORS(app)

# dictionary
me = {
    "name" : "Sergio",
    "last" : "Inzunza",
    "email" : "sinzunza@sdgku.edu",        
}

# list
products = data

@app.route("/")
@app.route("/home")
def index():
    return "Hello from Flask"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/about/name")
def name():
    return me["name"]


@app.route("/about/fullname")
def full_name():
    return me["name"] + " " + me["last"]



@app.route("/api/catalog")
def get_catalog():   
    cursor = db.products.find({})
    catalog = [item for item in cursor]    
    return parse_json(catalog)



@app.route("/api/catalog", methods=['POST'])
def save_product():    
    prod = request.get_json()
    db.products.insert(prod)
    return parse_json(prod)

    


@app.route("/api/catalog/id/<id>")
def get_producy_by_id(id):
    for prod in products:
        if(prod["_id"].lower() == id):
            return json.dumps(prod)

    abort(404)



@app.route("/api/catalog/cheapest")
def get_cheapest():
    cheapest = products[0]
    for prod in products:
        if(prod["price"] < cheapest["price"]):
            cheapest = prod

    return json.dumps(cheapest)



@app.route("/api/catalog/<category>")
def get_product_by_category(category):    
    data = db.products.find({ "category": category })
    results = [item for item in data]
    return parse_json(results)



@app.route("/api/categories")
def get_categories():
    data = db.products.find({})
    unique_categories = []
    # do the magic
    for prod in data:
        cat = prod["category"]

        # how to check if an element exist inside a list in python
        if cat not in unique_categories:
            unique_categories.append(cat)
            print(cat)
    return parse_json(unique_categories)



@app.route("/api/test")
def test_data_manipulation(): 
    test_data = db.test.find({})
    print(test_data)

    return parse_json(test_data[0])



#if __name__ == '__main__':
# app.run(debug=True)
# adding some awesome code that will fix everything
# another change