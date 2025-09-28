
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length
from datetime import datetime
import os
from dotenv import load_dotenv
from models import db, Vehicle, Salesperson, Customer, Sale
from database.seed.index import seed_database

# Load environment variables
load_dotenv()

# Create the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-for-demo-only')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost/car_dealership')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    # Check if database is empty and seed it if needed
    if Vehicle.query.count() == 0:
        seed_database()

# Forms
class VehicleForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired(), Length(max=50)])
    model = StringField('Model', validators=[DataRequired(), Length(max=50)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=datetime.now().year)])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    type = SelectField('Type', choices=[
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('hatchback', 'Hatchback')
    ])
    description = TextAreaField('Description', validators=[Length(max=500)])
    image_url = StringField('Image URL')
    submit = SubmitField('Save Vehicle')

class SalespersonForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=20)])
    hire_date = StringField('Hire Date', validators=[DataRequired()])
    submit = SubmitField('Save Salesperson')

class CustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Save Customer')

class SaleForm(FlaskForm):
    vehicle_id = SelectField('Vehicle', coerce=int, validators=[DataRequired()])
    customer_id = SelectField('Customer', coerce=int, validators=[DataRequired()])
    salesperson_id = SelectField('Salesperson', coerce=int, validators=[DataRequired()])
    sale_date = StringField('Sale Date', validators=[DataRequired()])
    sale_price = DecimalField('Sale Price', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save Sale')

# Routes
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')

    query = Vehicle.query
    if search:
        query = query.filter(Vehicle.make.ilike(f'%{search}%') | Vehicle.model.ilike(f'%{search}%'))

    vehicles = query.paginate(page=page, per_page=6, error_out=False)
    return render_template('index.html', vehicles=vehicles, search=search, now=datetime.now())

@app.route('/vehicle/<int:id>')
def vehicle_detail(id):
    vehicle = Vehicle.query.get_or_404(id)
    return render_template('details.html', vehicle=vehicle, now=datetime.now())

@app.route('/vehicle/create', methods=['GET', 'POST'])
def create_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        vehicle = Vehicle(
            make=form.make.data,
            model=form.model.data,
            year=form.year.data,
            price=form.price.data,
            type=form.type.data,
            description=form.description.data,
            image_url=form.image_url.data or None
        )
        db.session.add(vehicle)
        db.session.commit()
        flash('Vehicle created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html', form=form, title='Add Vehicle', now=datetime.now())

@app.route('/vehicle/edit/<int:id>', methods=['GET', 'POST'])
def edit_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    form = VehicleForm(obj=vehicle)
    if form.validate_on_submit():
        vehicle.make = form.make.data
        vehicle.model = form.model.data
        vehicle.year = form.year.data
        vehicle.price = form.price.data
        vehicle.type = form.type.data
        vehicle.description = form.description.data
        vehicle.image_url = form.image_url.data or None
        db.session.commit()
        flash('Vehicle updated successfully!', 'success')
        return redirect(url_for('vehicle_detail', id=vehicle.id))
    return render_template('edit.html', form=form, vehicle=vehicle, title='Edit Vehicle', now=datetime.now())

@app.route('/vehicle/delete/<int:id>', methods=['POST'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    flash('Vehicle deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/salesperson/create', methods=['GET', 'POST'])
def create_salesperson():
    form = SalespersonForm()
    if form.validate_on_submit():
        salesperson = Salesperson(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            hire_date=datetime.strptime(form.hire_date.data, '%Y-%m-%d').date()
        )
        db.session.add(salesperson)
        db.session.commit()
        flash('Salesperson created successfully!', 'success')
        return redirect(url_for('stats'))
    return render_template('create.html', form=form, title='Add Salesperson', now=datetime.now())

@app.route('/customer/create', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data
        )
        db.session.add(customer)
        db.session.commit()
        flash('Customer created successfully!', 'success')
        return redirect(url_for('stats'))
    return render_template('create.html', form=form, title='Add Customer', now=datetime.now())

@app.route('/sale/create', methods=['GET', 'POST'])
def create_sale():
    form = SaleForm()
    # Set default sale date to today
    form.sale_date.data = datetime.now().strftime('%Y-%m-%d')

    # Populate choices for dropdowns
    form.vehicle_id.choices = [(v.id, f"{v.year} {v.make} {v.model}") for v in Vehicle.query.all()]
    form.customer_id.choices = [(c.id, f"{c.first_name} {c.last_name}") for c in Customer.query.all()]
    form.salesperson_id.choices = [(s.id, f"{s.first_name} {s.last_name}") for s in Salesperson.query.all()]

    if form.validate_on_submit():
        sale = Sale(
            vehicle_id=form.vehicle_id.data,
            customer_id=form.customer_id.data,
            salesperson_id=form.salesperson_id.data,
            sale_date=datetime.strptime(form.sale_date.data, '%Y-%m-%d').date(),
            sale_price=form.sale_price.data
        )
        db.session.add(sale)
        db.session.commit()
        flash('Sale created successfully!', 'success')
        return redirect(url_for('stats'))
    return render_template('create.html', form=form, title='Add Sale', now=datetime.now())

@app.route('/stats')
def stats():
    # Get statistics for dashboard
    total_vehicles = Vehicle.query.count()
    total_sales = Sale.query.count()
    total_customers = Customer.query.count()
    total_salespeople = Salesperson.query.count()

    # Sales by month (for chart)
    sales_by_month = db.session.query(
        db.func.extract('month', Sale.sale_date).label('month'),
        db.func.count(Sale.id).label('count')
    ).group_by(db.func.extract('month', Sale.sale_date)).all()

    # Top selling vehicles
    top_vehicles = db.session.query(
        Vehicle.make,
        Vehicle.model,
        db.func.count(Sale.id).label('sales_count')
    ).join(Sale).group_by(Vehicle.id).order_by(db.func.count(Sale.id).desc()).limit(5).all()

    # Sales by salesperson
    sales_by_person = db.session.query(
        Salesperson.first_name,
        Salesperson.last_name,
        db.func.count(Sale.id).label('sales_count')
    ).join(Sale).group_by(Salesperson.id).order_by(db.func.count(Sale.id).desc()).all()

    # Vehicle types distribution
    vehicle_types = db.session.query(
        Vehicle.type,
        db.func.count(Vehicle.id).label('count')
    ).group_by(Vehicle.type).all()

    return render_template('stats.html', 
                         total_vehicles=total_vehicles,
                         total_sales=total_sales,
                         total_customers=total_customers,
                         total_salespeople=total_salespeople,
                         sales_by_month=sales_by_month,
                         top_vehicles=top_vehicles,
                         sales_by_person=sales_by_person,
                         vehicle_types=vehicle_types,
                         now=datetime.now())

@app.route('/api/vehicles')
def api_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        'id': v.id,
        'make': v.make,
        'model': v.model,
        'year': v.year,
        'price': float(v.price),
        'type': v.type,
        'description': v.description,
        'image_url': v.image_url
    } for v in vehicles])

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
