# Ryan Lau WeiChen Liu Daniel Liu
#SoftDev

#2022-09-22
#Time Spent:


"""
DISCO:
-random.randint() accepts two arguements, inclusive of both

QCC:


OPS SUMMARY:

"""

import random

krewes = {2:["WeiChen"],7:["Ryan"],8:["Daniel"]}

def select_random():
    rand = random.randint(0,2)
    print(rand)
    temp = 0
    if rand == 0:
        temp = 2
    elif rand == 1:
        temp = 7
    elif rand == 2:
        temp = 8
    return krewes[temp]

print(select_random())
    