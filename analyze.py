import numpy as np
import h5py as h5
import pandas as pd
import matplotlib.pyplot as plt
import os
# from scipy import stats
from sklearn.linear_model import LinearRegression
import csv
import globals

def analyze(file):
    lowerBound = 438
    upperBound = 460
    baslineThreshold = 5e6
    peak = 324.75
    peakMargin = 100
    saturation = 65535
    dir = "F:/LIBS/irisFitting3/"
    print("filenameGiven", file[0:8])
    try:
        temp = str(globals.assayData[globals.assayData['HOLEID'] == int(file[0:8])]['TCU']).split(" ")
        assayVal = globals.assayData['TCU'][int(temp[0])]
    except:
        return False
    

    try:
    
        with h5.File(os.path.join(dir+file+".001.h5")) as f:
            wavelength = f['wavelength'][...]
            intensity = f["intensity"][...]
            intensity = np.array(f['intensity'][...])
            wavelength = np.array(wavelength)

        # inputData = []
        # with open(os.path.join(dir,file), "r", newline='') as mycsv: 
        #     reader = csv.reader(mycsv, delimiter=",")
        #     for row in reader:
        #         inputData.append([float(i) for i in row])
        #         inputData = np.array(inputData)
        #         intensity = inputData[1:,:]
        #         wavelength = inputData[0, :]


            # print(wavelength[0:5])
            
            prevLength = wavelength.shape[0]
            # wavelength = wavelength[wavelength > 190]
            wavelength = wavelength[75:]
            newLength = wavelength.shape[0]
            intensity = intensity[:, prevLength-newLength:]
            
            prevLength = wavelength.shape[0]
            # wavelength = wavelength[wavelength < 950]
            wavelength = wavelength[0:7949]
            newLength = wavelength.shape[0]
            intensity = intensity[:, 0:intensity.shape[1]-(prevLength-newLength)]
            minBound = wavelength[wavelength < lowerBound].shape[0]
            maxBound = wavelength.shape[0] - wavelength[wavelength > upperBound].shape[0]
            # print(wavelength[wavelength < lowerBound].shape[0])
            # print(wavelength[wavelength[wavelength < lowerBound].shape[0]])
            wavelength = np.concatenate((wavelength[0:minBound], wavelength[maxBound:]), axis=0)
            intensity = np.concatenate((intensity[:,0:minBound], intensity[:,maxBound:]), axis=1)
            avg = np.mean(intensity[:], axis=0)
            processedFrames = np.zeros(intensity.shape[1])[np.newaxis]
            # print(processedFrames.shape)

            def find_nearest(array, value):
                array = np.asarray(array)
                idx = (np.abs(array - value)).argmin()
                return idx
            
            # if new:
            # #   print(list(wavelength))
            #     df = pd.DataFrame(wavelength)
            #     new = False

            # print(wavelength[50])
            keep = np.zeros(intensity.shape[0])[np.newaxis]
            # print("intensity shape", intensity.shape)
            # print("wavelength shape", wavelength.shape)
            # print(keep.shape)
            intensity = np.concatenate((intensity,keep.T), axis=1)
            # print("intensity with bool shape", intensity.shape, intensity[0][intensity.shape[1]-2])

            for frame in range(intensity.shape[0]):
                # for frame in range(5):
                # ind = 0
                # while(1):
                deleted = 0
                data = intensity[frame][0:intensity.shape[1]-1]
                baselineUV = data[find_nearest(wavelength, upperBound)]
                baselineVis = data[data.shape[0]-1]
                # baselineUV = f['intensity'][frame][f["intensity"].shape[1]-1]
                # baselineVis = f['intensity'][frame][f["intensity"].shape[1]-1]
                areaVis = baselineVis*(wavelength[wavelength.shape[0]-1] - wavelength[find_nearest(wavelength, upperBound)])
            
            if areaVis < baslineThreshold:
                # print(data[find_nearest(data, peak)-peakMargin:find_nearest(data, peak)+peakMargin])
                cuPeak = max(data[find_nearest(wavelength, peak)-peakMargin:find_nearest(wavelength, peak)+peakMargin])
                if cuPeak < saturation:
                    bound = find_nearest(wavelength, lowerBound)
                    data[0:bound] = abs(data[0:bound] - baselineUV)
                    data[bound:] = abs(data[bound:] - baselineVis)
                    intensity[frame][0:bound] = data[0:bound]
                    intensity[frame][bound:intensity.shape[1]-2]
                    intensity[frame][intensity.shape[1]-1] = 1
            else:
                deleted += 1
            processedFrames = np.mean(intensity[intensity[:,intensity.shape[1]-1] == 1, 0:intensity.shape[1]-1], axis=0)
            uv = find_nearest(wavelength, lowerBound)
            # normalizedIntensities = processedFrames[0:uv]/sum(processedFrames[0:uv])
            # wavelength = wavelength[0:uv]
            normalizedIntensities = processedFrames/sum(processedFrames)
            normalizedIntensities = normalizedIntensities * 3.5
            # print("normalized sahpe", normalizedIntensities.shape)
            # df["Sample "+file[6:17]] = normalizedIntensities
            # print("max", max(normalizedIntensities))
            plt.plot(wavelength[find_nearest(wavelength, 324):find_nearest(wavelength, 328)], normalizedIntensities[find_nearest(wavelength, 324):find_nearest(wavelength, 328)], label="Sample "+file[0:8])
            window = normalizedIntensities[find_nearest(wavelength, peak)-10:find_nearest(wavelength, peak)+10]
            # windowGrad = np.gradient(window)
            samplePeak = max(window)*100
            globals.data.append([samplePeak, assayVal, int(file[0:8])])
            return [samplePeak, assayVal, int(file[0:8])]
    except:
        return False



# print(analyze(str(17502452100)))