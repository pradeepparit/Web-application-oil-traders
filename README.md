## Project Overview
This project is a Flask-based web application designed for managing a store's inventory, user registration, login, and billing system. It integrates several core functionalities, such as user authentication, inventory management, and product billing. The project uses MySQL as the database backend and implements Flask-WTF for form validation, Flask-Login for user authentication, and pdfkit for generating PDFs of invoices.

## Key Features:
1. User Registration and Login: Users can register and login, with authentication handled via the Flask-Login extension.
2. Profile Management: Users can update their profile information, including shop details.
3. Product Management: Store products are added, updated, and tracked for quantity, price, and expiration.
4. Billing System: A dynamic billing system allows the generation of bills based on selected products, quantities, and prices.
5. PDF Invoice Generation: Generate downloadable invoices in PDF format.
6. Inventory Alerts: Automatic alerts for low stock, near-expiry, and expired products.
7. MySQL Integration: Data is stored in a MySQL database with models handled by SQLAlchemy.

## Technologies Used:
1. Flask: Web framework for building the server and handling requests.
2. Flask-WTF: For form validation.
3. Flask-Login: Manages user authentication.
4. Flask-SQLAlchemy: ORM for database operations.
5. MySQL: Database for storing user and product data.
6. pdfkit: For generating PDFs of invoices.


## Setup Instructions:
1. Requirements
- Python 3.x
- MySQL Database
- wkhtmltopdf (for PDF generation)

2. Required Python Packages:
- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy
- pdfkit
- WTForms

## Install required packages:
```bash
pip install Flask Flask-WTF Flask-Login Flask-SQLAlchemy pdfkit WTForms
```

## MySQL Setup:
Create a MySQL database and update the ```SQLALCHEMY_DATABASE_URI``` configuration in the app:
```bash
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost:3306/store'
```
Replace ```localhost```, ```root```, and ```store``` with your MySQL host, user, and database name.

## wkhtmltopdf Setup:
To enable PDF generation, install wkhtmltopdf and provide the path to the executable:
```bash
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
```
Make sure the path is correct according to your system configuration.

## Database Initialization:
Before running the application, initialize the database:
```bash
from app import db
db.create_all()
```
## Running the Application:
Run the Flask development server:
```bash
python app.py
```
Access the application at http://127.0.0.1:5000.

## Application Routes:
- ```/``` : Home page.
- ```/registration``` : User registration page.
- ```/login``` : Login page.
- ```/logout``` : Logout the current user.
- ```/profile``` : View the user's shop profile.
- ```/profile_update``` : Update the user's profile.
- ```/add_product``` : Add products to the store inventory.
- ```/dls``` : Display a list of products with current stock.
- ```/generate_bill``` : Create a bill for selected products.
- ```/pdf``` : Generate a PDF invoice.
- ```/search``` : Search products in the store.

## Database Models:
1. RegisterModel: Handles user registration details.

- Fields: id, username, password, shop_name, shop_type, shop_owner_name, shop_address, shop_start_date.

2. AddProduct: Handles product details.

- Fields: id, product_name, product_quantity, product_price, product_arrival_date, product_manufacture_date, product_expiry_date.

## Form Classes:
1. RegistrationForm: Form for user registration.
2. LoginForm: Form for user login.
3. update_profile: Form for updating user profile.
4. Product Form (implemented in the route ```/add_product```): Handles product details like name, quantity, price, and expiration.


## PDF Generation:
The application can generate a PDF bill for purchased products using pdfkit. Ensure that wkhtmltopdf is properly installed and the path is correctly set.
