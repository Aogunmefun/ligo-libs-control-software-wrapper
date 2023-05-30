import numpy as np
import h5py as h5
import matplotlib.pyplot as plt
import os
import csv

def predict(wavelength, intensity):
    labels = []
    lines = []
    lowerBound = 438
    upperBound = 460
    baslineThreshold = 5e6
    peak = 324.75
    peakMargin = 100
    saturation = 65535
    new = True
    peaks = []
    slope = 21.76
    intercept = -0.785

    print(intensity.shape)
        
    prevLength = wavelength.shape[0]
    wavelength = wavelength[wavelength > 190]
    newLength = wavelength.shape[0]
    intensity = intensity[prevLength-newLength:]

    prevLength = wavelength.shape[0]
    wavelength = wavelength[wavelength < 950]
    newLength = wavelength.shape[0]
    intensity = intensity[0:intensity.shape[0]-(prevLength-newLength)]
    minBound = wavelength[wavelength < lowerBound].shape[0]
    maxBound = wavelength.shape[0] - wavelength[wavelength > upperBound].shape[0]
    # print(wavelength[wavelength < lowerBound].shape[0])
    # print(wavelength[wavelength[wavelength < lowerBound].shape[0]])
    wavelength = np.concatenate((wavelength[0:minBound], wavelength[maxBound:]), axis=0)
    intensity = np.concatenate((intensity[0:minBound], intensity[maxBound:]), axis=0)
    # avg = np.mean(intensity[:], axis=0)
    processedFrames = np.zeros(intensity.shape[0])[np.newaxis]
    # print(processedFrames.shape)
    print("index", wavelength[1915])
    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return idx
    
    # print(wavelength[50])
    # keep = np.zeros(intensity.shape[0])[np.newaxis]
    # print("intensity shape", intensity.shape)
    # print("wavelength shape", wavelength.shape)
    # print(keep.shape)
    # intensity = np.concatenate((intensity,keep.T), axis=1)



    # for frame in range(5):
    # ind = 0
    # while(1):
    deleted = 0
    data = intensity
    baselineUV = data[find_nearest(wavelength, upperBound)]
    baselineVis = data[data.shape[0]-1]
    # baselineUV = f['intensity'][frame][f["intensity"].shape[1]-1]
    # baselineVis = f['intensity'][frame][f["intensity"].shape[1]-1]
    areaVis = baselineVis*(wavelength[wavelength.shape[0]-1] - wavelength[find_nearest(wavelength, upperBound)])
    
    # if areaVis < baslineThreshold:
    #     # print(data[find_nearest(data, peak)-peakMargin:find_nearest(data, peak)+peakMargin])
    #     cuPeak = max(data[find_nearest(wavelength, peak)-peakMargin:find_nearest(wavelength, peak)+peakMargin])
    #     if cuPeak < saturation:
    #         bound = find_nearest(wavelength, lowerBound)
    #         data[0:bound] = abs(data[0:bound] - baselineUV)
    #         data[bound:] = abs(data[bound:] - baselineVis)
    #         intensity[frame][0:bound] = data[0:bound]
    #         intensity[frame][bound:intensity.shape[0]-1]
    #         intensity[frame][intensity.shape[1]-1] = 1
    #     else:
    #         deleted += 1
    bound = find_nearest(wavelength, lowerBound)
    data[0:bound] = abs(data[0:bound] - baselineUV)
    data[bound:] = abs(data[bound:] - baselineVis)
    intensity[0:bound] = data[0:bound]
    # processedFrames = np.mean(intensity[intensity[:,intensity.shape[1]-1] == 1, 0:intensity.shape[1]-1], axis=0)
    processedFrames = intensity
    uv = find_nearest(wavelength, lowerBound)
    # normalizedIntensities = processedFrames[0:uv]/sum(processedFrames[0:uv])
    # wavelength = wavelength[0:uv]
    normalizedIntensities = processedFrames/sum(processedFrames)
    # normalizedIntensities = normalizedIntensities * 3.5
    # plt.plot(wavelength[find_nearest(wavelength, 324):find_nearest(wavelength, 328)], normalizedIntensities[find_nearest(wavelength, 324):find_nearest(wavelength, 328)])
    window = normalizedIntensities[find_nearest(wavelength, peak)-10:find_nearest(wavelength, peak)+10]
    # plt.plot(wavelength[1915-10:1915+10], normalizedIntensities[1915-10:1915+10])
    # windowGrad = np.gradient(window)
    samplePeak = max(window)*100
    value = (samplePeak*slope) + intercept
    print("Peak", samplePeak)
    print("value", value)
    plt.show()
    return value



# with h5.File("10501676150_23.5cm.001.h5") as f:
#     wavelength = np.array(f['wavelength'][...])
#     print("index", wavelength[1990])
#     # wavelength = wavelength.astype(int)

# row = 0
# with open("middleSample.csv","r") as my_csv:
#     rows = csv.reader(my_csv)
#     for spectra in rows:
#         if row == 0:
#             predict(wavelength, np.array(spectra).astype(float))
#         row+=1      
    

