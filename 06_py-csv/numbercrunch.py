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
on creating own random:
- 2 methods one creating a cumulative sum and dividing parts of it another creates multiple entries of a job in a list depending on percentage
- random.uniform()
QCC:
What type/object does csv.reader() return?
OPS SUMMARY:
-Uses csv.reader() to parse csv, seperates each field by "," or '"' for fields that contain a comma
-Csv.reader() will only read the second row to the second to last row
-loop through each line and construct dict of occupation:percent
V1:
-our random weight function works by checking if associated percent is 100. If not, find associated percent and multiply by 10. Append the percent 
to the array that number of times. Repeat for every key (occupation)
-Use randm.choice to get a "weighted" percent
V2:
- adds jobs to a new dictionary that uses the cumulative sum (previous sum + percentage) as the key
- random.uniform() generates a random number from 0 to final sum
- checks through dictionary keys for whether in range and returns the associate value of the key that the randNum is less than
"""

#imports
import csv
import random 

dict = {}

with open("occupations.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",",quotechar='"')
    rows_arr = list(csvreader)
    rows_arr = rows_arr[1:-1]
    for lines in rows_arr:
        occupation = lines[0]
        percent = float(lines[1])
        dict[occupation] = percent
    all_jobs = list(dict.keys())
    all_percents = list(dict.values())
    print(dict)

def doRandomWeights():
    #creates list and total slices
    arr = []
    total = 100
    # adds the job to the list corresponding number of times as percentage
    #(legal, legal, legal, education training and library, education training and library)
    for job in all_jobs:
        if dict[job] != total:
            percent = dict[job]
            #takes percent and multiplies by 10 to get rid of percent
            weighted = int(percent * 10)
        else:
            arr.append(job)
            break
        for i in range(weighted):
            arr.append(job)
    return random.choice(arr)


def doRandomWeights2():
    #create sum var and new dict
    sums = 0
    weights = {}
    #goes through jobs and makes cumulative sum to add to weights
    for job in all_jobs:
        percent = dict[job]
        sums += percent
        weights[sums] = job
    choice = random.uniform(0, sums)
    #goes through weights and if randNum is in range returns that entry
    for key in weights:
        if(choice < key):
            return weights[key]
    return 0
        
    
        
#randomWeightedJob = random.choices(all_jobs,weights=all_percents)
#print(randomWeightedJob)
for i in range(50):
    print("Output From The First Algorithm for Random Weights Is " + doRandomWeights())

for i in range(50):
    print("Output From The Second Algorithm for Random Weights Is " + doRandomWeights2())