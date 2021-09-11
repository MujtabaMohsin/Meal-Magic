import unittest
import json
from app import create_app
from config import *
from models import *


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        config_database(self.app)


        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)


    # --------- test get products , success ---------

    def test_get_products(self):
        res = self.client().get('/products', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # --------- test get cuisines , error ---------

    def test_get_cuisines_UNAUTHORIZED(self):
        res = self.client().get('/cuisines')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    # --------- test get cuisines , success ---------

    def test_get_cuisines_CUSTOMER(self):

        res = self.client().get('/cuisines', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # --------- test post cuisines , error ---------

    def test_post_cuisines_UNAUTHORIZED(self):
        res = self.client().post('/cuisines')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    # --------- test post product , error ---------

    def test_post_product_CUSTOMER(self):
        input_ = {'cuisine_id': 3, 'description': 'TEST', 'name': 'TEST', 'price': 68}
        res = self.client().post('/products', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN}, json=input_)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


    # --------- test post product , success ---------

    def test_post_product_COOKER(self):
        data = {'cuisine_id': 3, 'description': 'TEST', 'name': 'TEST2', 'price': 68}
        res = self.client().post('/products', headers={"Authorization": "Bearer " + COOKER_TOKEN}, json=data)
        data2 = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data2['success'], True)


        # --------- test post cuisine , success ---------

    def test_post_cuisines_MANGER(self):
        input_ = {'name': 'tes13t'}
        res = self.client().post('/cuisines', headers={"Authorization": "Bearer " + MANGER_TOKEN}, json=input_)
        data2 = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data2['success'], True)


    # --------- test patch product, success ---------

    def test_patch_product_COOKER(self):
        id = Product.query.order_by(Product.id.desc()).first().id
        input_ = {'cuisine_id': 3, 'description': 'TEST', 'name': 'TEST', 'price': 68}
        res = self.client().patch(f'/products/{id}', headers={"Authorization": "Bearer " + COOKER_TOKEN}, json=input_)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # --------- test patch product , error ---------

    def test_patch_product_UNAUTHORIZED(self):
        id = Product.query.order_by(Product.id.desc()).first().id
        input_ = {'cuisine_id': 3, 'description': 'TEST', 'name': 'TEST', 'price': 68}
        res = self.client().patch(f'/products/{id}', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN}, json=input_)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


    # --------- test patch cuisine , success ---------

    def test_patch_cuisine_Manger(self):
        id = Cuisine.query.order_by(Cuisine.id.desc()).first().id
        input_ = {'name': 'TEST000'}
        res = self.client().patch(f'/cuisines/{id}', headers={"Authorization": "Bearer " + MANGER_TOKEN}, json=input_)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # --------- test patch cuisine , error ---------

    def test_patch_cuisines_UNAUTHORIZED(self):

        id = Cuisine.query.order_by(Cuisine.id.desc()).first().id

        input_ = {'name': 'TEST000'}
        res = self.client().patch(f'/cuisines/{id}', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN}, json=input_)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


    # --------- test delete product , success ---------

    def test_delete_product_COOKER(self):
        id = Product.query.order_by(Product.id.desc()).first().id
        res = self.client().delete(f'/products/{id}', headers={"Authorization": "Bearer " + COOKER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # --------- test delete product , error ---------

    def test_delete_product_UNAUTHORIZED(self):

        id = Product.query.order_by(Product.id.desc()).first().id
        res = self.client().delete(f'/products/{id}', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    # --------- test delete cuisine , success ---------

    def test_delete_cuisine_Manger(self):
        id = Cuisine.query.order_by(Cuisine.id.desc()).first().id
        res = self.client().delete(f'/cuisines/{id}', headers={"Authorization": "Bearer " + MANGER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # --------- test delete cuisine , error ---------

    def test_delete_cuisines_UNAUTHORIZED(self):

        id = Cuisine.query.order_by(Cuisine.id.desc()).first().id
        res = self.client().delete(f'/cuisines/{id}', headers={"Authorization": "Bearer " + CUSTOMER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()




