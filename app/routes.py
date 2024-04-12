# routes.py
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Employee
from flask_migrate import Migrate

migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phonenumber = request.form['phonenumber']
        gender = request.form['gender']
        email = request.form['email']
         
        # Check if the email or phone number already exists
        if Employee.query.filter_by(email=email).first() is not None:
            flash('Email already exists.')
            return redirect(url_for('index'))
        if Employee.query.filter_by(phonenumber=phonenumber).first() is not None:
            flash('Phone number already exists.')
            return redirect(url_for('index'))
         
          
        # If not, create a new employee
        employee = Employee(firstname=firstname, lastname=lastname, phonenumber=phonenumber, gender=gender, email=email)
        db.session.add(employee)
        db.session.commit()
        flash('Employee added successfully!')
        return redirect(url_for('index'))
    else:
        # Retrieve sorting parameters from the query string
        sort_by = request.args.get('sort_by', 'firstname')  # Default sort by first name
        order_by = request.args.get('order_by', 'asc')  # Default order by ascending
        
        # Fetch employees based on sorting parameters
        if sort_by == 'firstname':
            employees = Employee.query.order_by(Employee.firstname.asc() if order_by == 'asc' else Employee.firstname.desc()).all()
        elif sort_by == 'lastname':
            employees = Employee.query.order_by(Employee.lastname.asc() if order_by == 'asc' else Employee.lastname.desc()).all()
        else:
            employees = Employee.query.all()
            
        return render_template('index.html', employees=employees)
    
    
@app.route('/update/<int:employee_id>', methods=['GET', 'POST'])
def update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    
    if request.method == 'POST':
        # Update employee details
        employee.firstname = request.form['firstname']
        employee.lastname = request.form['lastname']
        employee.phonenumber = request.form['phonenumber']
        employee.gender = request.form['gender']
        employee.email = request.form['email']
        
        # Commit changes to the database
        db.session.commit()
        flash('Employee details updated successfully!')
        return redirect(url_for('index'))
    
    return render_template('index.html', employee=employee)   
    
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        flash('Please enter a search query.')
        return redirect(url_for('index'))
    
    # Perform search based on first name or last name
    employees = Employee.query.filter(Employee.firstname.ilike(f'%{query}%') | Employee.lastname.ilike(f'%{query}%')).all()
    
    if not employees:
        flash('No employees found.')
    
    return render_template('index.html', employees=employees)


@app.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('index'))