# 10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen
# SoftDev
# 2022-10-06
#Time Spent: 0.4 Hour

"""
DISCO:

QCC:

OPS SUMMARY:

"""

import numbercruncher
from flask import Flask
app = Flask(__name__)

@app.route("/")
def disp_random_occ():
    jobDict = numbercruncher.generate_dict("occupations.csv") 
    s = ""
    s += "<h1 >10 items or fewer express checkout lane </h1> <h2> Daniel Liu, Anthony Sun, Jasmine Yuen </h2>"
    s += "<p>Your Best Bet Is the " + "<i>" + str(numbercruncher.give_weighted_job(jobDict)) + "</i>" + " Job" + "</p>"
    s += "All The Occupations Are: " + numbercruncher.get_all_occupations(jobDict)
    return s

app.debug = True
app.run()