import os
from flask import Flask, request, abort, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import *
from auth import *



def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    # Set up CORS and allow '*' for origins
    CORS(app, resources={'/': {'origins': '*'}})

    #  --------- set Access-Control-Allow ---------

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    # --------- ENDPOINTS ---------
    
    
    # --------- Basic ---------


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return redirect("https://muj-moshin.us.auth0.com/authorize?audience=Meal-Magic&response_type=token&client_id=0NffjGNrsa8sUVtytU0GYDsMTG514AJS&redirect_uri=https://meal-magic.herokuapp.com")


    @app.route('/logout')
    def login():
        return redirect("https://muj-moshin.us.auth0.com/v2/logout")

    # --------- Get Products ---------

    @app.route('/products')
    @requires_auth('get:products')
    def get_products(payload):
        # get all products from database
        products = Product.query.all()

        if products is None:
            abort(500);

        products_arr = []

        # products_arr is a list of dictionaries for each product for the json
        for product in products:
            products_arr.append(product.format_data())

        return jsonify({
            'success': True,
            'products': products_arr
        })

    # --------- Get Cuisines ---------

    @app.route('/cuisines')
    @requires_auth('get:cuisines')
    def get_cuisines(payload):
        # get all cuisines from database
        cuisines = Cuisine.query.all()

        if cuisines is None:
            abort(500);

        cuisines_arr = []

        # cuisines_arr is a list of dictionaries for each product for the json
        for cuisine in cuisines:
            cuisines_arr.append(cuisine.format_data())

        return jsonify({
            'success': True,
            'cuisines': cuisines_arr
        }), 200

    # --------- Post Product ---------

    @app.route('/products', methods=['POST'])
    @requires_auth('post:products')
    def post_product(payload):
        data = request.get_json()
        # print(data)
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        cuisine_id = data.get('cuisine_id')

        if name is None or description is None or price is None or cuisine_id is None:
            abort(404)

        # add the product
        new_product = Product(name=name, description=description, price=price, cuisine_id=cuisine_id)

        # insert to the database
        new_product.insert()

        return jsonify({
            'success': True,
            'product': new_product.format_data()

        })

    # --------- Post Cuisine ---------

    @app.route('/cuisines', methods=['POST'])
    @requires_auth('post:cuisines')
    def post_cuisine(payload):
        data = request.get_json()

        name = data.get('name')

        if name is None:
            abort(404)

        # add the cuisine
        new_cuisine = Cuisine(name=name)

        # insert to the database
        new_cuisine.insert()

        return jsonify({
            'success': True,
            'cuisine': new_cuisine.format_data()

        })

    # --------- Patch Product ---------

    @app.route('/products/<int:product_id>', methods=['PATCH'])
    @requires_auth('patch:products')
    def patch_product(payload,product_id):
        data = request.get_json()

        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        cuisine_id = data.get('cuisine_id')

        if name is None or description is None or price is None or cuisine_id is None:
            abort(404)

        # get the product
        product = Product.query.filter_by(id=product_id).first()
        if not product:
            abort(404)

        # update the product
        product.name = name
        product.description = description
        product.price = price
        product.cuisine_id = cuisine_id

        product.update()

        return jsonify({
            'success': True,
            'product': product.format_data()

        })

    # --------- Patch Cuisine ---------

    @app.route('/cuisines/<int:cuisine_id>', methods=['PATCH'])
    @requires_auth('patch:cuisines')
    def patch_cuisine(payload,cuisine_id):
        data = request.get_json()

        name = data.get('name')

        if name is None:
            abort(404)

        # get the cuisine
        cuisine = Cuisine.query.filter_by(id=cuisine_id).first()
        if not cuisine:
            abort(404)

        # update the product
        cuisine.name = name

        cuisine.update()

        return jsonify({
            'success': True,
            'cuisine': cuisine.format_data()

        })

    # --------- Delete Product ---------

    @app.route('/products/<int:product_id>', methods=['DELETE'])
    @requires_auth('delete:products')
    def delete_product(payload,product_id):
        # get the question you want to delete
        product = Product.query.filter_by(id=product_id).first()

        if product is None:
            abort(422)

        product.delete()

        return jsonify({
            'success': True,
            'message': "The product is deleted"
        })

    # --------- Delete Cuisine ---------

    @app.route('/cuisines/<int:cuisine_id>', methods=['DELETE'])
    @requires_auth('delete:cuisines')
    def delete_cuisine(payload,cuisine_id):
        # get the question you want to delete
        cuisine = Cuisine.query.filter_by(id=cuisine_id).first()

        if cuisine is None:
            abort(422)

        cuisine.delete()

        return jsonify({
            'success': True,
            'message': "The cuisine is deleted"
        })


    # --------- Error Handling  ---------

    @app.errorhandler(422)
    def unprocessable_422(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def unprocessable_400(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Permissions not found'
        }), 400

    @app.errorhandler(500)
    def unprocessable_500(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error'
        }), 500

    @app.errorhandler(404)
    def unprocessable_404(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unathorized'
        }), 401



    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
