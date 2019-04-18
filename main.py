from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=["POST"])
def validation():
    # grab all the submitted data
    user_name = request.form['username']
    user_pass = request.form['password']
    rep_pass = request.form['rep_password']
    e_mail = request.form['email']

    # create empty error strings to fill if there's an error later on
    user_name_error = ""
    user_pass_error = ""
    rep_pass_error = ""
    e_mail_error = ""

    # if no error occurs, this remains True, and the redirect to welcome occurs
    # otherwise, the main page will reload

    # if any of these conditions trigger, the should_redirect variable will set to False,
    # and each one handles the error
    if len(user_name) < 3 or len(user_name) > 20:
        user_name_error = "That's not a valid username"

    if len(user_pass) < 3 or len(user_pass) > 20:
        user_pass_error = "That's not a valid password"

    if user_pass != rep_pass:
        rep_pass_error = "Passwords do not match"
 

    if e_mail != "" and (len(e_mail) < 3 or len(e_mail) > 20 or ("@" not in e_mail) or ("." not in e_mail) or (" " in e_mail)):
        e_mail_error = "Passwords do not match"

    if (not user_name_error) and (not user_pass_error) and (not rep_pass_error) and (not e_mail_error):
        return render_template("welcome.html", user_name=user_name)

    return render_template("index.html", username=user_name, user_name_error=user_name_error, 
        password="", user_pass_error=user_pass_error, rep_pass="", rep_pass_error=rep_pass_error, 
        email=e_mail, e_mail_error=e_mail_error)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

app.run()