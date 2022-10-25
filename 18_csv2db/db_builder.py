#Team ADS

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="database.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def convert(row):
    for i in range(len(row)):
        if row[i].isnumeric():
            row[i]= int(row[i])
    temp = str(row).strip("[").strip("]")
    return tuple(temp)
            
#==========================================================

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute("CREATE TABLE amunals (name TEXT, age NUMERIC, id INTEGER PRIMARY KEY);")    # run SQL statement

with open("courses.csv","r") as filename:
    dictreader = csv.reader(filename)
    for row in dictreader:
        c.execute()

with open("students.csv","r") as filename:
    dictreader = csv.reader(filename)
    for row in dictreader:
        c.execute()

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


