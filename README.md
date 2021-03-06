# Meal-Magic
Meal Magic is web API was created as the capstone project for Udacity's Full-Stack Developer Nanodegree program. It aims to apply all the concepts and skills gained.
It models a food company that serve food products from differnt cuisines. 

## Site Link
https://meal-magic.herokuapp.com/

## Knowledge and Technologies Used
- Python
- Relational Database
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Flask 
- Authentication and Access
- Auth0
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications
- Heroku

## Getting Started
### Run Locally
1.	Clone the repository
```
git clone https://github.com/MujtabaMohsin/Meal-Magic.git
```

2.	Install Dependencies
```
pip install -r requirements.txt
```

3.	Create a database using PostgreSQL
```
createdb Meal-Magic
```
or import the database included dirictly

4.	Update the database url in the config.py file
```
.
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/Meal-Magic"
.
```

5.	Run the app
```
python app.py
```

## API Reference

### Roles
There are three roles in this API:

**1.  Customer:** can get all products and cuisines only

**2.  Cooker:** can do all actions for products but can only get cuisines

**3.  Manger:** can do all actions

### Login
To use the API, you need log in and to be authenticated. Then a Jwt token would be generated.
To login, you should move to the ```/login``` enfpoint such as https://meal-magic.herokuapp.com/login then the access token will be genereted in the URI
according the user roles.

Three dummy accounts were created as follow:
##### User 1
- **Role**: Customer
- **Username**: user-customer@email.com
- **Password**: User1234!

##### User 2
- **Role**: Cooker
- **Username**: user-cooker@email.com
- **Password**: User1234!

##### User 3
- **Role**: Manger
- **Username**: user-manger@email.com
- **Password**: User1234!

### Endpoints
**GET /products** : returns all the products.

Sample of success results:
```
{
    "products": [
        {
            "name": "Sweet and Sour Pork",
            "description": "Sweet and sour pork is a Chinese dish particularly popular in westernised Cantonese cuisine",
            "cuisine_id": 3,
            "price": 68
        }
    ],
    "success": true
}
```

**GET /cuisines** : returns all the cuisines.

Sample of success results:
```
{
    "cuisines": [
        {
            "id": 1,
            "name": "Arab"
        },
        {
            "id": 2,
            "name": "Chinese"
        },
        {
            "id": 3,
            "name": "Indian"
        }
    ],
    "success": true
}
```

In case no token was entered, error masseage would be shown
```
{
    "error": 401,
    "message": "Authorization header is expected.",
    "success": false
}
```

**POST /products** : post a new product

**POST /cuisines** : post a new cuisine
 
**PATCH /products/<int:id>** : update a specific product by id

**PATCH /cuisines/<int:id>** : update a specific cuisine by id

**DELETE /products/<int:id>** : delete a specific product by id
 
**DELETE /cuisines/<int:id>** : delete a specific cuisine by id


## Test
To run the tests, run:
```
python test_app.py
```
it should disply the ok message if all tests passed
```
Ran 15 tests in 35.333s

OK
```

NOTE: The tokens available in config.py will be expaired. So you need to update them manually.
