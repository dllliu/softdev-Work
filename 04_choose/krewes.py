# Ryan Lau WeiChen Liu Daniel Liu
#SoftDev
#K04-DictWord
#2022-09-22
#Time Spent: 0.4 Hour


"""
DISCO:
-random.randint() accepts two arguements, inclusive of both
-You Can Access The Value Pair By Using The Key as the "Index"

QCC:
-How Can We Manually Generate Random-Ness Without Importing Random?

OPS SUMMARY:
-First we wrote the heading. Then we initialized the dictionary of
period:students as the key:value pairs. Then we imported random and
then made functions to first choose the random period, then another
function to return a random student or ducky based on the output of the random period function.
"""

import random

krewes = {2:["WeiChen","David"],7:["Ryan","<T>"],8:["Daniel","Porky"]}

def select_random_period():
    rand = random.randint(0,2)
    #print(rand)
    temp = 0
    if rand == 0:
        temp = 2
    elif rand == 1:
        temp = 7
    elif rand == 2:
        temp = 8
    return krewes[temp]


def select_random_student(students):
    rand = random.randint(0,len(students)-1)
    return students[rand]

    
#print(select_random_period())
print(select_random_student(select_random_period()))
    