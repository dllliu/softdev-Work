#Talia Daniel Dynamic Turtles
#SoftDev
#06
#2022-09-28
#Time Spent: 0.8 Hour

"""
DISCO:
-csv module
-csv.reader() function takes in params like delimiter and quotechar
-delimiter specifies the character used to separate each field. The default is the comma (',')
-quotechar specifies the character used to surround fields that contain the delimiter character. The default is a double quote (' " ').

QCC:
What type/object does csv.reader() return?

OPS SUMMARY:
-Uses csv.reader() to parse csv, seperates each field by "," or '"' for fields that contain a comma
-loop through each line and construct dict of occupation:percent 
-our random weight function works by checking if associated percent is 100. If not, find associated percent and multiply by 10. Append the percent 
to the array that number of times. Repeat for every key (occupation)
-Use randm.choice to get a "weighted" percent
"""

import csv
import random 

dict = {}

with open("occupations.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",",quotechar='"')
    for lines in csvreader:
        occupation = lines[0]
        percent = float(lines[1])
        dict[occupation] = percent
    all_jobs = list(dict.keys())
    all_percents = list(dict.values())


def doRandomWeights():
    arr = []
    total = 100
    for job in all_jobs:
        if dict[job] != total:
            percent = dict[job]
            weighted = int(percent * 10)
        else:
            return dict[job]
        for i in range(weighted):
            arr.append(job)
    return random.choice(arr)
        
#randomWeightedJob = random.choices(all_jobs,weights=all_percents)
#print(randomWeightedJob)
print(doRandomWeights())
