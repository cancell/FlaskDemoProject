from cgitb import text
import email
from xmlrpc.client import boolean
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login',  methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    if request.method =="POST":
        email = request.form.get("email")
        firstname = request.form.get("firstName")
        password = request.form.get("password1")
        password2 = request.form.get("password2")
        if len(email) < 4:
            flash("Email is too short!! Must be greater than 4 characters.", category="error")
        elif len(firstname) < 2:
            flash("Firstname is too short!! Must be greater than 2 characters.", category="error")
        elif password != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password) < 7:
            flash("Password is too short!! Must be greater than 7 characters.", category="error")
        else:
            flash("Account creared.", category="success")
            #add database
    return render_template("sign_up.html")