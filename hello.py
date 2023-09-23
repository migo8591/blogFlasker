from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from wtforms.widgets import TextArea

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rebHaraya314@localhost/our_users"
app.config['SECRET_KEY']="mySuperSecretKey"
db.init_app(app)
migrate = Migrate(app, db)
#json thing:
@app.route('/date')
def get_current_date():
    favorite_pizza ={
        "William": "Pepperoni",
        "Evelyn": "Cheese",
        "Daniela":"Supreme"
    }
    # return {"Date": date.today()}
    return favorite_pizza

#**********Create model**********:
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True )
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    favorite_color=db.Column(db.String(120))
    date_added=db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(120))

    @property 
    def password(self):
        raise AttributeError('Password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    # Create a string
    def __repr__(self):
        return '<Name %r>' % self.name
    # The serialize method converts the object to a dictionary
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "emai": self.email
        }
#Create a blog post model:
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default= datetime.utcnow)
    slug = db.Column(db.String(255))
with app.app_context():
    db.create_all()
#******************Create a form Class*******************:
class UserForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    email=StringField("Email", validators=[DataRequired()])
    favorite_color=StringField("Favorite color")
    password_hash= PasswordField("Password",validators=[DataRequired(), EqualTo('password_hash2', message='Password must mathc!')])
    password_hash2= PasswordField("Confirm password",validators=[DataRequired()])
    submit=SubmitField("Submit") 
class NamerForm(FlaskForm):
    name=StringField("what's your name", validators=[DataRequired()])
    submit=SubmitField("Submit") 
class PasswordForm(FlaskForm):
    email=StringField("what's your email", validators=[DataRequired()])
    password_hash=PasswordField("What's your password", validators=[DataRequired()])
    submit=SubmitField("Submit") 
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    author = StringField("Author", validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")
#****************** Routes *******************:
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
@app.route('/add_user', methods=['GET','POST'])
def add_user():
    name=None
    formulario=UserForm()
    if formulario.validate_on_submit():
        user=Users.query.filter_by(email=formulario.email.data).first() 
        if user is None:
            #Hash the password!!!
            hashed_pw=generate_password_hash(formulario.password_hash.data, "sha256")
            user=Users(name=formulario.name.data, email=formulario.email.data, favorite_color=formulario.favorite_color.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        name=formulario.name.data
        formulario.name.data=''    
        formulario.email.data='' 
        formulario.favorite_color.data='' 
        formulario.password_hash.data='' 
        flash("User added successfully!")     
    our_users=Users.query.order_by(Users.date_added)
    return render_template("add_user.html",form=formulario, name=name, our_users=our_users )
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']
        try:
            db.session.commit()
            flash("User update successfully")
            # return render_template("add_user.html", form=form, name_to_update=name_to_update)
            return redirect(url_for("add_user"))
        except:
            flash("Error! Looks like there was a problem...Try again!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
            print(name_to_update)
            return render_template("update.html", form=form, name_to_update=name_to_update, identificator=id)
@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Users.query.get_or_404(id)
    name = None
    formulario = UserForm()
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully")
        our_users=Users.query.order_by(Users.date_added)
        return render_template("add_user.html",form=formulario, name=name, our_users=our_users )
    except:
        flash("Whoop! There was a problem deleting user, try again..")
        return render_template("add_user.html",form=formulario, name=name, our_users=our_users )
#Create Custom Error Pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
#Create Password Test Page:
def user(name):
    return render_template("user.html", nombre=name)
@app.route('/test_pw', methods=['GET','POST'])
def test_pw():
    email=None
    password = None
    pw_to_check = None
    passed = None
    form=PasswordForm()
    # Validate Form
    if form.validate_on_submit():
        email=form.email.data
        password=form.password_hash.data
        #Clear the form
        form.email.data=''
        form.password_hash.data=''
        #Lookup User by email address
        pw_to_check = Users.query.filter_by(email=email).first()
        #Check hashed password
        passed = check_password_hash(pw_to_check.password_hash, password)
    return render_template("test_pw.html", email=email, password = password, pw_to_check=pw_to_check, passed=passed, form=form)
@app.route('/add-post', methods=['GET', 'POST'])
def addPost():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author=form.author.data,slug=form.slug.data)
        form.title.data = ''
        form.content.data = ''
        form.author.data = ''
        form.slug.data = ''
        #Add post data to database:
        db.session.add(post)
        db.session.commit()
        flash("Blog Post Submitted Successfully!")
    return render_template("add_post.html", form = form)
@app.route("/posts")
def posts():
    #Grab all the posts from the databases:
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("posts.html", posts= posts)
@app.route('/posts/<int:id>')
def post(id):
    post = Posts.query.get_or_404(id)
    return render_template('post.html', post=post)

#git:
#I_could_have_done_that}
# BooleanField, DateField, DateTimeField, DecimalField, FileField, HiddenField, MultipleField, FieldList, FloatField, FormField, IntegerField, PassworldField, RadioField, SelectField, SelectMultipleField, SubmitField, StringField, TextAreaField 

"""
Validators: DataRequired, email, EqualTo, InputRequired, IPAddress, Length, MacAddress, NumberRange, Optional, Regexp, UUID (numero de identificación de usuario únicof), AnyOf, NoneOf
"""
#video 15
#https://youtu.be/FYsPj40aQoc?list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&t=433
#revise: https://www.bogotobogo.com/python/Flask/Python_Flask_Blog_App_with_MongoDB.php
#visa diversity: https://www.ustraveldocs.com/cr/en/immigrant-visa/#kvisa
"""
accesibilidad web:
https://www.linkedin.com/learning/desarrollo-web-accesible-esencial/que-es-la-accesibilidad-y-por-que-deberia-aplicarla?autoSkip=true&resume=false
stay out of it = no te metas
do your thing = haz lo tuyo
don't worry 
https://www.facebook.com/reel/860395495649666
https://www.facebook.com/reel/2519648291524810
https://www.facebook.com/reel/845043140240706
https://www.facebook.com/reel/1284000912220574
https://www.facebook.com/reel/608370418138582
Responsive portfolio: https://www.youtube.com/watch?v=-uQIBlaZ4P0
crea una pagina web desde cero: https://www.youtube.com/watch?v=HH_SMpxV7qQ
better teacher: https://www.youtube.com/watch?v=qmyicviEZck
better2: https://www.youtube.com/watch?v=0V0WeEnsec0
in on at: https://www.youtube.com/watch?v=lEiWK6huZck
pypal y nexjs: https://www.youtube.com/watch?v=ouqcQunk0fU
"""