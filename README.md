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

