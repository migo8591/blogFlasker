from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    username=StringField("Username", validators=[DataRequired()])
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
    # content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    content = CKEditorField('Content', validators=[DataRequired()])
    # author = StringField("Author")
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# https://azure.microsoft.com/en-us/free/students/
# https://techcommunity.microsoft.com/t5/microsoft-learn-blog/introducing-a-new-resource-for-all-role-based-microsoft/ba-p/3500870?id=msftsource_issue51F1email_gdc%3Focid%3Deml_pg410653_gdc_comm_mw&mkt_tok=MTU3LUdRRS0zODIAAAGOUh199syjeLTr2BZWCJOO-xieOnSu8ShldV7OILpLbvynTjiTUpWt5mTkPp7aq-hqhvKWM-AW68GvZvaf9_phJ688_Dve5xVcE8CUsCjEM8m3fAG3_eTx9QsX
#https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/

# osoft Post Conversation Survey BotMinimizeEnd conversation
# Start
# Read
# Privacy
# OK, let's get started. What kind of Azure help do you need?
# Business/Personal
# Student
# Azure Partners
# Student
# Read
# What kind of help do you need?
# Azure for Students
# Sign-up Issues
# Azure for Students
# Read
# Is there anything else I can help you with today?
# Yes
# No
# Yes
# Read
# OK, let's get started. What kind of Azure help do you need?
# Business/Personal
# Student
# Azure Partners
# Student
# Read
# What kind of help do you need?
# Azure for Students
# Sign-up Issues
# Sign-up Issues
# Read
# Is there anything else I can help you with today?
# Yes
# No
# Yes
# Read
# OK, let's get started. What kind of Azure help do you need?
# Business/Personal
# Student
# Azure Partners
# Business/Personal
# Read
# What kind of help do you need?
# Sign-up Issues
# Technical/Billing support
# Pricing Estimates
# Live Chat with Sales
# Live Chat with Sales
# Read
# I'll connect you with the Azure sales team now.
#  at 10:30, Sep 26:
# Just a minute while I transfer you.
#  at 10:30, Sep 26:
# You can correspond with us at your convenience during this conversation. Miral will be with you shortly.
#  at 10:31, Sep 26:

# Welcome to Microsoft Azure Sales, my name is Miral; Can I start by getting your Full name please?
# Migue Muñoz Catedral
# Read
#  at 10:32, Sep 26:

# It is my pleasure talking to you Migue
# What brought you to our website today?
# I would like to know if Microsoft will have this year a free certification for exam Azure -900.? One time I participed in Microsoft Build and you gifted a offer...
# Read
# Do you know when Microosoft to do Build?
# Read
#  at 10:35, Sep 26:

# Sure thing, and It's awesome to see that you are interested in Azure cloud services, it is one of our most popular and used services
#  at 10:35, Sep 26:

# Moments to check your query please
#  at 10:35, Sep 26:

# May I ask you just to help you further, do you have Azure account?
# thanks
# Read
# yes
# Read
#  at 10:36, Sep 26:

# Did you try Azure free trail?
# Yes I used it by I would like certify me in Azure for looking up a job
# Read
# But this certification has a cost $60 in Costa Rica
# Read
#  at 10:38, Sep 26:

# Sure, I got you
#  at 10:38, Sep 26:

# Do you have a budget in mind for the exam?
# Yes...
# Read
#  at 10:39, Sep 26:

# In this case my best recommendation would be to arrange for a free consultation of a Microsoft Azure partner who is specialized in dealing with Azure cloud services and through this contact, they will help you through answering your questions regarding features, prices, and licensing and give you the most cost-effective options for your requirements with more customized options and prices to meet your business needs and budget .
#  at 10:39, Sep 26:

# the consultation is done through email address or a phone call based on your preference


# I will proceed now with the contact request once I get your okay

# Shall we proceed with the consultation?
#  at 10:39, Sep 26:

# They will let you get it
#  at 10:39, Sep 26:

# I just need - Full name.
# - Email / mobile phone and address (city name and zip code / postal code).
#  at 10:42, Sep 26:

# Are we still connected?
# Miguel Angel Muñoz Catedral - miguel.munoz@uned.cr - +506 89106806 - San José, Costa Rica 10101 - 11501
# Read
#  at 10:43, Sep 26:

# Thank you for the information. Now that I have the required info and I’ll process this case now for you. The contact will be within the next 2-3 business days and I will send you their info via email so you can reach them sooner if you need, would you prefer that I set the method for the initial contact to be through email or phone call ?
#  at 10:43, Sep 26:

# I flagged it as ASAP contact for you
# I would like to be contact throught email...
# Read
# thanks for your help...
# Read
#  at 10:45, Sep 26:

# Awesome, I will send you the names of the partners now, quick moments please to proceed this for you
# Ok I am going to wait.
# Read
#  at 10:46, Sep 26:

# Thank you so much for waiting, here are the names of the partners who will contact you very soon.
# [Database Technologies], [Consulting Group Corporacion Latinoamericana], [GRUPO BABEL SOCIEDAD ANONIMA]
#  at 10:46, Sep 26:

# And that's my professional email: (v-miralsadeq@microsoft.com) feel free to contact
# me directly if you need any further assistance.
#  at 10:46, Sep 26:

# It has been a pleasure talking to you today, I am hoping that your chat with me was satisfactory, would there be anything that I can provide, for me to ensure that I've assisted you to my fullest extent today, Miguel?
# Thanks.... I do not need anything else. Thanks for you help
# Read
#  at 10:48, Sep 26:

# Most welcome I am always at your help
#  at 10:48, Sep 26:

# It was my pleasure talking to you today, I am hoping that your chat with me was satisfactory.


# And your feedback is important to us, please stay in this chat window to get your feedback about this Microsoft experience if this is okay with you of course.

# Thank you for contacting Microsoft Azure Sales Team.
# Please take care and have an awesome day ahead :).
#  at 10:48, Sep 26:

# Goodbye ❤️