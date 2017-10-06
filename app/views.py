"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from wtforms import DecimalField, DateField, TextField, Form, IntegerField, SelectField, validators, PasswordField, ValidationError

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
    startdate = DateField('startdate', format ='%d/%m/%y')
    duration = IntegerField('duration', [validators.Required()])
    salary = DecimalField('salary', [validators.Required()])
    retention = DecimalField('retention', [validators.Required()])
    


@app.route('/addEmployee/', methods = ['POST','GET'])
def addEmployee():
    form = EmployeeForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate():
            fname = request.form['fname']
            lname = request.form['lname']
            position = request.form['position']
            location = request.form['location']
            startdate = request.form['startdate']
            duration = request.form['duration']
            salary = request.form['salary']
            retention = request.form['retention']
            
            
            basicSalary = salary - retention
            
            newEmp = employee(fname,lname,position,location,startdate,duration,salary,retention,basicSalary)
            db.session.add(newEmp)
            db.session.commit()
            
            
        flash('New employee has been registered successfully', 'success')
    return render_template("addEmployee.html", form = form)
    

@app.route('/view')
def list_profiles():
    """route for viewing list of profiles"""
    return render_template('view.html', employees=employee.query.all())

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
