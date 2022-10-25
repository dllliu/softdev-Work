import csv

with open("students.csv","r") as filename:
    dictreader = csv.reader(filename)
    for row in dictreader:
        for i in range(len(row)):
            if row[i].isnumeric():
                row[i]= int(row[i])
        temp = str(row).strip("[").strip("]")
        print(tuple(row))

            


