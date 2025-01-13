# Inventory Management System

This project is an **Inventory Management System** built with **Django**. It provides a user-friendly interface to manage products, suppliers, sales orders, and stock movements. The system helps businesses track their inventory levels, manage supplier information, and process sales orders.

## Features

- **Product Management**
  - View, create, edit, and delete products.
  - Track product details such as name, description, price, stock quantity, and supplier information.

- **Supplier Management**
  - Manage supplier information such as name, email, phone, and address.
  - Add, update, and delete suppliers.

- **Sales Order Management**
  - Create and manage sales orders with product, quantity, total price, status, and date.

- **Stock Movement Management**
  - Track incoming and outgoing stock movements.
  - Manage stock with detailed notes and movement dates.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB (using Djongo)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/inventory-management.git
cd inventory-management
```

### 2. Set up Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the migrations to set up the database:

```bash
python manage.py migrate
```

### 5. Create a Superuser

To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

### 7. Access the Application

Visit the following URL in your browser to access the application:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

To access the Django admin panel, visit:

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Log in using the superuser credentials you created earlier.

## Project Structure

```
inventory_management/
├── inventory/
│   ├── migrations/
│   ├── static/
│   │   └── inventory/
│   │       ├── css/
│   │       │   └── styles.css
│   │       └── js/
│   │           └── scripts.js
│   ├── templates/
│   │   └── inventory/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       └── product_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── inventory_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Models

The system has the following main models:

- **Product**: Represents a product in the inventory.
- **Supplier**: Represents a supplier who provides products.
- **SaleOrder**: Represents a sales order for a product.
- **StockMovement**: Represents the movement of stock (incoming or outgoing).

## URLs

- **/products/**: Displays the list of products.
- **/products/new/**: Create a new product.
- **/products/<int:pk>/**: View product details.
- **/suppliers/**: Displays the list of suppliers.
- **/suppliers/new/**: Create a new supplier.
- **/sales_orders/**: Displays the list of sales orders.
- **/sales_orders/new/**: Create a new sales order.
- **/stock_movements/**: Displays the list of stock movements.
- **/stock_movements/new/**: Create a new stock movement.

## Static Files

- **CSS**: All styles are located in `inventory/static/inventory/css/styles.css`.
- **JS**: JavaScript functionalities are located in `inventory/static/inventory/js/scripts.js`.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
