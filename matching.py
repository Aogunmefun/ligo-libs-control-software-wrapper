import numpy as np
import csv

sampleids = []
assays = []
indexes = []
unwanted = []

with open("assays.csv","r", newline='') as my_csv:
    reader = csv.reader(my_csv, delimiter=",")
    for row in reader:
        assays.append(row[0][0:4]+row[3][:])


with open("sampleids.csv","r", newline='') as my_csv:
    reader = csv.reader(my_csv, delimiter=" ")
    for row in reader:
        # print(row)
        sampleids.append("".join(row[0:2]))

sampleids[0] = sampleids[0][3:]

for ind in range(len(sampleids)):
    # try:
    #     unwanted.index(sampleids[ind])
    #     print("removed", sampleids[ind])
    # except:
        
    try:
        indexes.append(assays.index(sampleids[ind]))
    except:
        print("no match found for: ", sampleids[ind])
        unwanted.append(ind)
   


print("indexes", indexes)
print("length", len(indexes))
print("unwanted", unwanted)

# print("ids", sampleids[1])
# print("assays", assays[2])
# print("indexes", indexes)