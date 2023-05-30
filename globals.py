import numpy as np

channel1 = 0
channel2 = 0
pixels1 = 4096
pixels2 = 4096
wavelength1 = [0.0] * 4096
wavelength2 = [0.0] * 4096
spectraldata1 = [0.0] * 4096
spectraldata2 = [0.0] * 4096
scan = False
maxFrames = 50
scans = 0
uvExposure = 10000
visibleExposure = 2500
measconfig1 = ""
measconfig2 = ""
fileName = "my measurement"
spectra = ""
wavelengths = ""
tower1 =  np.array([
    [-10,-67,7],
    [-40,-66.8,7],
    [0,0,2],
    [0,0,3]
])
tower2 = np.array([
    [0,0]
])