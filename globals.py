import numpy as np
import socket

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
    [-10,-66.8,7],
    [-40,-67.5,7],
    [-70,-69,7],
    [-101,-70.5,7],
    [-132,-72,7],
    [-164,-73.5,7],
    [-196,-75,7.5],
    [-228,-75.5,8],
    [-261,-75.5,9.5],
    [-292.5,-75.5,9.5]
])
tower2 = np.array([
    [0,0]
])
robot = socket.socket()