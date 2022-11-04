# ADS: Ayman Habib, Sam Lubelsky, Daniel Liu
# Softdev pd02
# k1
# 2022-11-03
# time spent: 1.0 hr

from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os 

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

username = "ads"
password = "admin"

@app.route('/')
def index():
    if 'username' in session:
        return render_template('response.html',username = session['username'])
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    '''
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        print(userIn)
        print(passIn)
        if(userIn != username):
            resp = make_response(render_template("error.html", msg = "wrong username"),404)
            return resp
        elif passIn != password:
            resp = make_response(render_template("error.html", msg = "wrong password"),404)
            return resp
        else:
            session['username'] = request.form['username']
            resp = render_template('response.html',username = session['username'])
            return resp
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
    