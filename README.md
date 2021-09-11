# Meal-Magic
Meal Magic is web API was created as the capstone project for Udacity's Full-Stack Developer Nanodegree program. It aims to apply all the concepts and skills gained.
It models a food company that serve food products from differnt cuisines. 

## Site Live
https://meal-magic.herokuapp.com/

## Knowledge and Technologies Used
• Python

• Relational Database

• Modeling Data Objects with SQLAlchemy

• Internet Protocols and Communication

• Flask 

• Authentication and Access

• Auth0

• Role-Based Access Control (RBAC)

• Testing Flask Applications

• Deploying Applications

• Heroku

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

**1.	Customer:** can get all products and cuisines only
**2.	Cooker:** can do all actions for products but can only get cuisines
**3.	Manger:** can do all actions

### Endpoints
**GET /products** : returns all the products.
Sample of results:
```
{

}
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
Sample of results:
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

**POST /products** : post a new product

**POST /cuisines** : post a new cuisine
 
**PATCH /products/<int:id>** : update a specific product by id

**PATCH /cuisines/<int:id>** : update a specific cuisine by id

**DELETE /products/<int:id>** : delete a specific product by id
 
**DELETE /cuisines/<int:id>** : delete a specific cuisine by id
