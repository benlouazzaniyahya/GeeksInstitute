
from datetime import datetime, date
from database.index import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    sales = db.relationship('Sale', backref='vehicle', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Vehicle {self.year} {self.make} {self.model}>'

class Salesperson(db.Model):
    __tablename__ = 'salespeople'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    sales = db.relationship('Sale', backref='salesperson', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Salesperson {self.first_name} {self.last_name}>'

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    sales = db.relationship('Sale', backref='customer', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id', ondelete='CASCADE'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)
    salesperson_id = db.Column(db.Integer, db.ForeignKey('salespeople.id', ondelete='CASCADE'), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    sale_price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Sale {self.id} - Vehicle {self.vehicle_id}>'
