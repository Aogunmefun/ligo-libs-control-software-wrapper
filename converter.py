# What I'm doing in this script is just demonstrating reading and writing to .h5 files. Basically, I'm going to be reading an already
# existing .h5 file that was generated by Iris CC. I'll then copy these values and use them to create a new .h5 file called test



import h5py as h5 # This is the module I'm using for reading and writing
import numpy as np
import csv


with h5.File("10501676150_23.5cm.001.h5") as f:
    # print(f.keys())
    # val = print(f['aux'])
    # print(f['channel'])
    # print(f['channelName'])
    # print(f['frame'])
    # print(f['intensity'])
    # print(f['order'])
    # print(f['saturationCount'])
    # print(f['series'])
    # print(f['settings'].keys())
    # print(f['timeReceived'])
    # print(f['timeReceivedLocal'])
    # print(f['timeRecorded'])
    # print(f['wavelength'])
    # arr = f['intensity'][0][:]
    wavelength = f['wavelength'][:]
    formatVersion = f.attrs['formatVersion']



def convertFile(name):
    data = []
    with open(name+".csv","r", newline='') as my_csv:
        reader = csv.reader(my_csv, delimiter=",")
        # data = reader
        for row in reader:
            data.append([float(i) for i in row])
    
    with h5.File(name+'.h5', 'w') as f:
        f.attrs['formatVersion'] = formatVersion
        f.create_group('aux')
        f.create_dataset('channel', data = [0, 1])
        f.create_dataset('channelName', data=[b'7213303SP',b'7213304SP'])
        f.create_dataset('frame', data=np.arange(0,9999))
        f.create_dataset('intensity', data=data[1:][:])
        f.create_dataset('order', data=np.zeros(shape=(8188,1)))
        f.create_dataset('saturationCount', data=[0])
        f.create_dataset('series', data=[50])
        settings = f.create_group('settings')
        settings.create_dataset('exposureTime', data=[[10000],[2500]])
        settings.create_dataset('isAveraged', data=[0])
        settings.create_dataset('isDarkMeasurement', data=[0])
        settings.create_group('laser')
        f.create_dataset('timeReceived', data=[[1680129854923344],[1680129854916598]])
        f.create_dataset('timeReceivedLocal', data=[[1680104654923344],[1680104654916598]])
        f.create_dataset('timeRecorded', data=[[22393.30211],[22395.37896]])
        f.create_dataset('wavelength', data=wavelength)

convertFile("F:/LIBS/fitting/"+str(17001273550))

        