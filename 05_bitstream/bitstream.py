#Talia Daniel
#SoftDev
#05
#2022-09-28
#Time Spent: 0.4 Hour


"""
DISCO:
split() function
read in file into a big string and split that into multiple entries
adding stuff to dictionaries
random.randrange()

QCC:

OPS SUMMARY:
We opened and read the file into a string. We used the split function to first divide the entries for each person, and then divided that into
the devo and their ducky. We then made the keys of the dictionary the periods(2,7,8) and appended the contents for each entry into their respective keys.
Finally, we chose a random period and random ducky within that period, and then printed the output in a formatted string.
"""
import random

dict = {}

def read_file(file_name):
    file1 = open(file_name)
    string = file1.read()
    each_entry = string.split("@@@")
    for i in each_entry:
        contents = i.split("$$$")
        period = contents[0]
        if period not in dict:
            dict[period] = [] #new empty array
        dict[period].append((contents[1],contents[2]))


def get_random_ducky():
    random_period = random.choice(list(dict.keys()))
    random_ducky = dict[random_period][random.randrange(len(dict[random_period]))]
    return (f"{random_period}:{random_ducky[0]}:{random_ducky[1]}")

#print(dict)
read_file("krewes.txt")
duck = get_random_ducky()
print(duck)
