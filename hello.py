from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rebHaraya314@localhost/our_users"
app.config['SECRET_KEY']="mySuperSecretKey"
db.init_app(app)

#Create model:
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True )
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    date_added=db.Column(db.DateTime, default=datetime.utcnow)
    # Create a string
    def __repr__(self):
        return '<Name %r>' % self.name
    # The serialize method converts the object to a dictionary
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
with app.app_context():
    db.create_all()
#Create a form Class:
class UserForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    email=StringField("Email", validators=[DataRequired()])
    submit=SubmitField("Submit") 
@app.route('/add_user', methods=['GET','POST'])
def add_user():
    name=None
    formulario=UserForm()
    if formulario.validate_on_submit():
        user=Users.query.filter_by(email=formulario.email.data).first() 
        if user is None:
            user=Users(name=formulario.name.data, email=formulario.email.data)
            db.session.add(user)
            db.session.commit()
        name=formulario.name.data
        formulario.name.data=''    
        formulario.email.data='' 
        flash("User added successfully!")     
    our_users=Users.query.order_by(Users.date_added)
    return render_template("add_user.html",form=formulario, name=name, our_users=our_users )
class NamerForm(FlaskForm):
    name=StringField("what's your name", validators=[DataRequired()])
    submit=SubmitField("Submit") 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", nombre=name)
@app.route('/name', methods=['GET','POST'])
def name():
    name=None
    form=NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash("Form Submitted Successfully!")
    return render_template("name.html", name=name, form=form)

#Create Custom Error Pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
#git:
#I_could_have_done_that}
# BooleanField, DateField, DateTimeField, DecimalField, FileField, HiddenField, MultipleField, FieldList, FloatField, FormField, IntegerField, PassworldField, RadioField, SelectField, SelectMultipleField, SubmitField, StringField, TextAreaField 

"""
Validators: DataRequired, email, EqualTo, InputRequired, IPAddress, Length, MacAddress, NumberRange, Optional, Regexp, UUID (numero de identificación de usuario únicof), AnyOf, NoneOf
"""


#revise: https://www.bogotobogo.com/python/Flask/Python_Flask_Blog_App_with_MongoDB.php