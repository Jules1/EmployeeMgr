"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from wtforms import TextAreaField, DecimalField, DateField, TextField, Form, IntegerField, SelectField, validators, PasswordField, ValidationError
from datetime import datetime, timedelta
from app import db
from app import employee

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
class EmployeeForm(Form):
    firstn = TextField('firstn', [validators.Required()])
    lastn = TextField('lastn', [validators.Required()])
    position = TextField('position', [validators.Required()])
    location = TextField('location', [validators.Required()])
    startdate = DateField('startdate', format ='%d/%m/%y', render_kw={"placeholder":"dd/mm/yyyy"})
    duration = IntegerField('duration', [validators.Required()], render_kw={"placeholder":"duration in weeks"})
    salary = DecimalField('salary', [validators.Required()])
    retention = DecimalField('retention', [validators.Required()])

class SearchForm(Form):
    firstn = TextField('firstn', [validators.Required('Please enter first name before searching')])

class appraiseForm(Form):
    score = IntegerField('score',[validators.Required()], render_kw={"placeholder":"Appraisal Rating"})
    notes = TextAreaField('notes', [validators.Required()], render_kw={"placeholder":"Notes about employee"})

class vacationForm(Form):
    vacDays = IntegerField('vacDays', [validators.Required()], render_kw={"placeholder":"Amount of vacation days granted"})

@app.route('/addEmployee/', methods = ['POST','GET'])
def addEmployee():
    form = EmployeeForm(csrf_enabled=False)
    if request.method == 'POST':
        #if form.validate():
        fname = request.form['firstn']
        lname = request.form['lastn']
        position = request.form['position']
        location = request.form['location']
        startdate = datetime.strptime(request.form['startdate'], "%d/%m/%y")
        duration = int(request.form['duration'])
        salary = float(request.form['salary'])
        retention = float(request.form['retention'])
        
        enddate = startdate + timedelta(weeks=duration)
        basicSalary = salary - retention
        
        newEmp = employee(firstname = fname, lastname =lname,position=position,location=location,startdate=startdate,duration=duration,salary=salary,retention=retention,netBasicSalary=basicSalary, enddate = enddate)
        db.session.add(newEmp)
        db.session.commit()
        
        
        flash('New employee has been registered successfully', 'success')
    else:
        flash("Employee not added, please enter all fields", "danger")
    return render_template("addEmployee.html", form = form)
    

@app.route('/view')
def list_profiles():
    """route for viewing list of profiles"""
    return render_template('view.html', employees=employee.query.all())

@app.route('/search', methods=['POST', 'GET'])
def searchEmp():
    """route to search for employee"""
    form = SearchForm(csrf_enabled=False)
    if request.method == 'POST':
        found = employee.query.filter_by(firstname = request.form['firstn']).all()
        if found is None:
           flash('No employee by that name was found', 'danger')
           return render_template('search.html', form=form)
        else:
           flash('The following employees were found', 'success') 
        return render_template('search.html', form=form, employees=found)
    
    return render_template('search.html', form=form)

@app.route('/empProfile/<empid>', methods=['POST','GET'])
def empProfile(empid):
    """Information for a singular profile"""
    emp = employee.query.filter_by(id = empid).all()
    return render_template('empProfile.html', employees=emp)

@app.route('/Appraisal/<empid>', methods=['POST', 'GET'])
def appraise(empid):
    """Form to add employee appraisal"""
    form = appraiseForm(csrf_enabled=False)
    emp = employee.query.filter_by(id = empid).all()
    if request.method=='POST':
        emp = employee.query.filter_by(id = empid).update(dict(score = int(request.form['score']), empNotes = request.form['notes']))
        db.session.commit()
        flash("Appraisal has been submitted", "success")
        return render_template('home.html')
    else:
        flash("Something went wrong","danger")
    return render_template('appraisal.html', form=form, emp=emp)

@app.route('/Vacation/<empid>', methods=['POST','GET'])
def vacation(empid):
    """form to schedule vacation days"""
    form = vacationForm(csrf_enabled=False)
    emp = employee.query.filter_by(id=empid).all()
    if request.method == 'POST':
        emp.vacation += int(request.form['vacDays'])
        emp.vacationBalance = emp.vacationBalance - emp.vacation
        emp.sickLeaveBalance = emp.sickLeaveBalance - emp.vacation
        db.session.commit()
        return render_template('vacationUpdate.html',form=form, emp = emp)
    return render_template('vacationUpdate.html', form=form, emp=emp)

@app.route('/Sick/<empid>', methods=['POST','GET'])
def sick(empid):
    return render_template('sickDays.html')
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
