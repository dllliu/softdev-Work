# ADS: Ayman Habib, Sam Lubelsky, Daniel Liu
# Softdev pd02
# k19
# 2022-11-03
# time spent: 1.0 hr

from flask import Flask             #facilitate flask webserving
from flask import render_template, make_response   #facilitate jinja templating
from flask import request, session, redirect, url_for          #facilitate form submission
import os 

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)


username = "ads"
password = "admin"

@app.route('/', methods=['GET','POST'])
def login():
    if username in session:
        return f'Logged in as {session["username"]}'
    return render_template('login.html')
    
'''
    session['username'] = request.form.get('username')
    return render_template('login.html')
'''

@app.route("/login", methods=['GET', 'POST'])
def authenticate():
    userIn = request.form.get('username')
    passIn = request.form.get('password')
    if(userIn != username):
        resp = make_response(render_template("error.html", msg = "wrong username"))
        return resp
    elif passIn != password:
        resp = make_response(render_template("error.html", msg = "wrong password"))
        return resp 
    else:
        session['username'] = request.form['username']
        #resp = make_response(render_template('response.html',username=userIn))
        #return resp
        return render_template('response.html',username = userIn)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
