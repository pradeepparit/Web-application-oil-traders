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
