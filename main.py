from flask import Flask, request, redirect, render_template
import cgi
import string

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup-home.html')

@app.route('/', methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    good_username = True
    good_password = True
    good_verify = True
    good_email = True
    if username == "":
        username_error = "Please enter a username"
        good_username = False
    if password == "":
        password_error = "Please enter a password"
        good_password = False
    if len(username) < 3 or len(username) > 20:
        username = ""
        username_error = "Username must be between 3 and 20 characters."
        good_username = False
    for character in username:
        if character in string.punctuation or character in string.whitespace:
            username_error = username + " is not a valid username, please do not use spaces or special characters"
            username = ""
            good_username = False
    if not password == verify:
        verify_error = "Password inputs do not match. Please try again."
        good_verify = False
    if verify == "":
        verify_error = "Please reenter your password"
        good_verify = False
    if not email == "":
        if "@" not in email and "." not in email:
            email_error = "Please enter a valid email"
            email = ""
            good_email = False
        if len(email) < 3 or len(email) > 20:
            email_error = "Please enter a valid email"
            email = ""
            good_email = False
    if good_username and good_password and good_verify and good_email:
        return render_template('welcome.html', username=username)
    else:
        return render_template("signup-home.html", username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
    
    

app.run()