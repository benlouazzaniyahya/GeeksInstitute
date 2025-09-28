
# Car Dealership Management System

A full-stack web application for managing a car dealership's inventory, salespeople, customers, and sales transactions.

## Features

- **Vehicle Management**: Add, view, edit, and delete vehicle listings with images
- **Salesperson Management**: Manage dealership staff information
- **Customer Management**: Track customer details for sales records
- **Sales Tracking**: Record and track vehicle sales
- **Search & Pagination**: Search vehicles by make/model with pagination (6 items per page)
- **Dashboard & Analytics**: View statistics and charts for sales performance
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Visualization**: Chart.js
- **Icons**: Font Awesome

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd car-dealership
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**
   - Create a new PostgreSQL database named `car_dealership`
   - Update the `DATABASE_URL` in your `.env` file if needed (see below)

5. **Create a `.env` file** in the project root with the following content:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://username:password@localhost/car_dealership
   ```
   Replace `username` and `password` with your PostgreSQL credentials.

6. **Run the application**
   ```bash
   python index.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Database Schema

The application uses the following database schema:

### Tables

1. **vehicles**
   - id (Primary Key)
   - make
   - model
   - year
   - price
   - type
   - description
   - image_url
   - created_at

2. **salespeople**
   - id (Primary Key)
   - first_name
   - last_name
   - email
   - phone
   - hire_date
   - created_at

3. **customers**
   - id (Primary Key)
   - first_name
   - last_name
   - email
   - phone
   - address
   - created_at

4. **sales**
   - id (Primary Key)
   - vehicle_id (Foreign Key)
   - customer_id (Foreign Key)
   - salesperson_id (Foreign Key)
   - sale_date
   - sale_price
   - created_at

## Project Structure

```
car-dealership/
├── index.py              # Main Flask application
├── models/
│   ├── __init__.py
│   └── your_model.py     # Database models
├── database/
│   ├── index.py          # Database connection
│   └── seed/
│       ├── __init__.py
│       ├── index.py      # Database seeding script
│       └── index.sql     # SQL schema and seed data
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # List view
│   ├── create.html       # Create form
│   ├── edit.html         # Edit form
│   ├── details.html      # Detail view
│   └── stats.html        # Statistics page
└── requirements.txt      # Python dependencies
```

## Usage

### Adding a Vehicle

1. Click "Add Vehicle" in the navigation bar
2. Fill in the vehicle details
3. Submit the form

### Managing Inventory

- View all vehicles on the homepage
- Search vehicles by make/model
- View, edit, or delete individual vehicles
- Navigate through pages using pagination

### Tracking Sales

1. Add salespeople and customers
2. Create sales records linking vehicles to customers and salespeople
3. View sales analytics on the dashboard





