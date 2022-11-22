# X-Treme Blockers Daniel, Nicholas
# Softdev pd02
# k20
# 2022-11-21
# time spent: 0.6 hr

from flask import *
import requests

nasa_url = "https://api.nasa.gov/planetary/apod?api_key="

f = open("key_nasa.txt","r")
key = f.read()
complete_url = nasa_url + key

app = Flask(__name__)    #create Flask object

@app.route("/")
def index():
    r = requests.get(complete_url).json()
    img_url = r["url"]
    img_exp = r["explanation"]
    return render_template("main.html",img_url = img_url, img_exp = img_exp)
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()