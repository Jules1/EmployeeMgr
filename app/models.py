from . import db

class employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key="True")
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    position = db.Column(db.String(30))
    location = db.Column(db.String(30))
    startdate = db.Column(db.Date)
    duration = db.Column(db.Integer)
    enddate = db.Column(db.Date)
    vacationEnt = db.Column(db.Integer)
    vacationtaken = db.Column(db.Integer)
    vacationBalance = db.Column(db.Integer)
    sickLeaveTaken = db.Column(db.Integer)
    sickLeaveBalance = db.Column(db.Integer)
    leaveNoPay = db.Column(db.Integer)
    salary = db.Column(db.Float)
    retention = db.Column(db.Float)
    netBasicSalary = db.Column(db.Float)
    score = db.Column(db.Integer)

##    def __repr__(self):
##        return '<Employee %r %r %r>' % (self.firstname, self.lastname, self.position)
    
    