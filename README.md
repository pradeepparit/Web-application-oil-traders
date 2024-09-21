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
