import csv
import numpy as np
import matplotlib.pyplot as plt


data = []
xaxis = []
count = 0
with open("F:/LIBS/fitting3/17001273550.csv","r", newline='') as my_csv:
    reader = csv.reader(my_csv, delimiter=",")
    # data = reader
    for row in reader:
        if count == 0:
            xaxis = [float(i) for i in row]
            xaxis = np.array(xaxis)
            print("x-axis", xaxis[0:5])
            count +=1
        else:
            row = [float(i) for i in row]
            row = np.array(row)
            print("y-axis", row[0:5])
            plt.plot(xaxis[0: xaxis.shape[0]-3], row[0:row.shape[0]-3])
            plt.show()
        
# data = np.array(data)

# data = np.array(data)
# print(data[0, 0:5])
# plt.plot(data[0,:], data[500, :])
# plt.show()