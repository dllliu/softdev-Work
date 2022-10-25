# ADS: Ayman Habib, Sam Lubelsky, Daniel Liu
# Softdev pd02
# k17-18
# 2022-10-25
# time spent: 0.7 hr

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="school.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def convert(row):
    for i in range(len(row)):
        if row[i].isnumeric():
            row[i]= int(row[i])
    return tuple(row)
            
#==========================================================

c.execute("DROP TABLE if exists students")
c.execute("DROP TABLE if exists courses")
c.execute("CREATE TABLE courses (name TEXT, age NUMERIC, id NUMERIC);")    # run SQL statement
c.execute("CREATE TABLE students (name TEXT, age NUMERIC, id NUMERIC);")

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open("courses.csv","r") as filename:
    dictreader = csv.reader(filename)
    next(dictreader)
    for row in dictreader:
        row = convert(row)
        c.execute("INSERT INTO courses VALUES " + str(row) + ";")

with open("students.csv","r") as filename:
    dictreader = csv.reader(filename)
    next(dictreader)
    for row in dictreader:
        row = convert(row)
        c.execute("INSERT INTO students VALUES " + str(row) + ";")

#==========================================================

db.commit() #save changes
db.close()  #close database


