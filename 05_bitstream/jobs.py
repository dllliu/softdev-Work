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

dict = {}

def read_file(file_name):
    file1 = open(file_name)
    string = file1.read()
    each_entry = string.split("\n")
    for i in each_entry:
        print(i)
        if (each_entry[0] == '"'):
            contents = i.split('"')
        else:
            contents = i.split(",")
        dict[contents[0]] = []
    dict[contents[0]].append((contents[1]))
    return dict

print(read_file("test.csv"))
"""
import random
  
  
sampleList = [100, 200, 300, 400, 500]
  
randomList = random.choices(
  sampleList, weights=(10, 20, 30, 40, 50), k=5)
  
print(randomList)
"""