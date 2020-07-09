#!/usr/bin/python3

import flask
from flask import request, jsonify

app = flask.Flask(__name__)

app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'Flask Web Development: Developing Web Applications with Python',
     'author': 'Miguel Grinberg',
     'first_sentence': 'Learn Flask Web Development.',
     'year_published': '2014'},
    {'id': 1,
     'title': 'Mastering Flask',
     'author': 'Jack Stouffer',
     'first_sentence': 'Learn Mastering Flask.',
     'published': '2015'},
    {'id': 2,
     'title': 'Flask Framework Cookbook: Over 80 Proven Recipes and Techniques for Python Web',
     'author': 'Shalabh Aggarwal',
     'first_sentence': 'Learn Falsk Framework.',
     'published': '2019'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Let's Reading Books</h1>
<p>A prototype endpoint API for distant reading of bookss.</p>'''


@app.route('/api/v1/sources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/sources/books', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)


    return jsonify(results)

app.run()