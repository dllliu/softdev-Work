#Talia Daniel
#SoftDev
#05
#2022-09-28
#Time Spent: 0.4 Hour


"""
DISCO:

QCC:

OPS SUMMARY:

"""
import random

file1 = open("krewes.txt")
string = file1.read()

each_entry = string.split("@@@")
dict = {}

for i in each_entry:
    contents = i.split("$$$")
    period = contents[0]
    if period not in dict:
        dict[period] = [] #new empty array
    dict[period].append((contents[1],contents[2]))


def get_random_ducky():
    random_period = random.choice(list(dict.keys()))
    random_ducky = dict[random_period][random.randrange(len(dict[random_period]))]
    return (f"{random_period}:{random_ducky[1]}")

print(dict)
duck = get_random_ducky()
print(duck)
