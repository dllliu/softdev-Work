#Talia Daniel
#SoftDev
#06
#2022-09-28
#Time Spent: 0.8 Hour

"""
DISCO:
atom adds a new line upon save (extra time to debug because i edited csv)

QCC:

OPS SUMMARY:

"""
import random

dict = {}

file1 = open("occupations.csv")
string = file1.read()
each_entry = string.split("\n")
for i in each_entry:
    if '"' in i:
        parsed_arr = i.strip('"').split('"')
    else:
        parsed_arr = i.split(",")
    print(parsed_arr)
    print(parsed_arr[1])
    occupation = parsed_arr[0]
    percentage = float(parsed_arr[1].replace(",",""))
    dict[percentage] = []
    dict[percentage].append(occupation)
    
print(dict)

all_percents = tuple(dict.keys())
all_occupations_arr = list(dict.values())
randomWeightedPercent = random.choices(all_occupations_arr,weights=(all_percents))
print(randomWeightedPercent)

#print(dict[all_percents[random.randrange(len(all_percents))]])
