from flask import Flask, render_template, flash, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from webforms import LoginForm, PostForm, PasswordForm, NamerForm, UserForm, SearchForm 
from flask_ckeditor import CKEditor

db = SQLAlchemy()
app = Flask(__name__)
ckeditor = CKEditor(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rebHaraya314@localhost/our_users"
app.config['SECRET_KEY']="mySuperSecretKey"
db.init_app(app)
migrate = Migrate(app, db)
# Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
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
class Users(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(20), nullable=False, unique=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    favorite_color=db.Column(db.String(120))
    date_added=db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(120))
    #User can have many posts
    posts = db.relationship('Posts', backref='poster')

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
    #author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default= datetime.utcnow)
    slug = db.Column(db.String(255))
    # Foreing key to link Users(refer to primary of the user)
    poster_id= db.Column(db.Integer, db.ForeignKey('users.id'))
with app.app_context():
    db.create_all()
#****************** Routes *******************:
# Pass Stuff To Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)
# Create Search Function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    posts = Posts.query
    if form.validate_on_submit():
        #Get data from submitted from
        post.searched = form.searched.data
        #Query the Databases / tipo de concatenacion
        posts = posts.filter(Posts.content.like('%'+post.searched+'%'))
        posts = posts.order_by(Posts.title).all()
        return render_template("search.html", form=form, searched=post.searched, posts = posts)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/admin')
@login_required
def admin():
    id = current_user.id
    if id == 43:
        return render_template("admin.html")
    else:
        flash("Sorry you must be the Admin to ")
        return redirect(url_for('dashboard'))
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
            user=Users(username=formulario.username.data,name=formulario.name.data, email=formulario.email.data, favorite_color=formulario.favorite_color.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        name=formulario.name.data
        formulario.name.data=''    
        formulario.username.data=''    
        formulario.email.data='' 
        formulario.favorite_color.data='' 
        formulario.password_hash.data='' 
        flash("User added successfully!")     
    our_users=Users.query.order_by(Users.date_added)
    return render_template("add_user.html",form=formulario, name=name, our_users=our_users )
@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.username = request.form['username']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']
        try:
            db.session.commit()
            flash("User update successfully")
            # return render_template("add_user.html", form=form, name_to_update=name_to_update)
            return redirect(url_for("dashboard"))
        except:
            flash("Error! Looks like there was a problem...Try again!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
            print(name_to_update)
            return render_template("update.html", form=form, name_to_update=name_to_update, id=id)
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
        # return render_template("add_user.html",form=formulario, name=name, our_users=our_users )
        return redirect(url_for('add_user'))
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
@app.route("/posts")
def posts():
    #Grab all the posts from the databases:
    posts = Posts.query.order_by(Posts.date_posted)
    print(posts)
    return render_template("posts.html", posts = posts)
@app.route('/add-post', methods=['GET', 'POST'])
def addPost():
    form = PostForm()
    if form.validate_on_submit():
        poster = current_user.id
        post = Posts(title=form.title.data, content=form.content.data, poster_id=poster,slug=form.slug.data)
        form.title.data = ''
        form.content.data = ''
        # form.author.data = ''
        form.slug.data = ''
        #Add post data to database:
        db.session.add(post)
        db.session.commit()
        flash("Blog Post Submitted Successfully!")
        posts = Posts.query.order_by(Posts.date_posted)
        print("Lo que tiene es: ",posts)
        return redirect(url_for('posts'))
    return render_template("add_post.html", form = form)
@app.route('/posts/<int:id>')
def post(id):
    post = Posts.query.get_or_404(id)
    form = PostForm()
    form.content.data=post.content
    return render_template('post.html', post=post, form= form)
@app.route('/post/edit/<int:id>', methods=['GET','POST'])
def edit_post(id):
    post = Posts.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        # post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        # Update Database:
        db.session.add(post)
        db.session.commit()
        flash("Post has been updated!")
        return redirect(url_for('posts'))
    if current_user.id == post.poster_id:
        form.title.data=post.title
        # form.author.data=post.author
        form.slug.data=post.slug
        form.content.data=post.content
        return render_template('edit_post.html', form=form)
    else:
        flash("You Aren't Authorized to Edit This Post...")
        return redirect(url_for('posts'))
@app.route('/posts/delete/<int:id>')
@login_required
def delete_post(id):
    post_to_delete=Posts.query.get_or_404(id)
    id = current_user.id
    #Si la persona coincide con la que creo la publicacion...
    if id == post_to_delete.poster.id:
        try:
            db.session.delete(post_to_delete)
            db.session.commit()
            #Return a message
            flash("Blog Post Was Deleted!")
            #Grab all the posts from the databases:
            # posts = Posts.query.order_by(Posts.date_posted)
            # return render_template("posts.html", posts= posts)
            return redirect(url_for('posts'))
        except:  
            flash("Whoops! There was a problem deleting post")      
            #Grab all the posts from the databases:
            posts = Posts.query.order_by(Posts.date_posted)
            return render_template("posts.html", posts= posts)
    else:
        flash("You Aren't Authorized to Delete This Post")
        return redirect(url_for('posts'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(username=form.username.data).first()
        if user:
            #check the hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Successfull!!")
                return redirect(url_for('dashboard'))
            else:
                flash("Wrong Password - Try Again!")
        else:
            flash("That User Doesn't Exist! Try Again...")
    return render_template('login.html', form=form)
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You Have Been Logged Out! Thanks for stopping by...")
    return redirect(url_for('login'))
#API Express:  https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/?fbclid=IwAR3z5XwbkNFt2AB3aTjE1uGPFbQiQzp2Ce_ZlmdAzvpYiyuiWfgcC4BZyvM
#I_could_have_done_that}
# BooleanField, DateField, DateTimeField, DecimalField, FileField, HiddenField, MultipleField, FieldList, FloatField, FormField, IntegerField, PassworldField, RadioField, SelectField, SelectMultipleField, SubmitField, StringField, TextAreaField 

"""
see vrs watch: https://www.facebook.com/reel/699385911793089
Validators: DataRequired, email, EqualTo, InputRequired, IPAddress, Length, MacAddress, NumberRange, Optional, Regexp, UUID (numero de identificación de usuario únicof), AnyOf, NoneOf
"""
#video 15
#
#revise: https://www.bogotobogo.com/python/Flask/Python_Flask_Blog_App_with_MongoDB.php
#visa diversity: https://www.ustraveldocs.com/cr/en/immigrant-visa/#kvisa
"""
review R:https://www.youtube.com/watch?v=bDHBdUrBr5k&ab_channel=RenzoCaceresRossi
POO python freeCode: https://youtu.be/Ej_02ICOIgs
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
evelina: 
https://www.youtube.com/shorts/kdZhisSuxmY?t=17&feature=share
TuTORIAL BOX-MODEL: 
https://youtu.be/WfDqFArJnYA?t=4852
inner:
https://youtube.com/shorts/STtvuH6c_JI?si=pGOKpAUnun9shZkw


        <h4 class="card-title">Wel</h4>

"""

#https://www.linkedin.com/learning/diseno-para-programacion-esencial/el-proceso-creativo?autoSkip=true&resume=false


#accesibility:
#hace 3 años aria:
#https://www.youtube.com/watch?v=38JDscMbB4I&list=PLadWW12WRDFNrIb1jHDWso76xb2m3oLtz&ab_channel=WebAccessibilityEducation
#What is wai-aria
#https://www.youtube.com/watch?v=CNoz0TXG-vk