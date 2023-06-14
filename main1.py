import socket
import eel
import eel.browsers
from time import sleep
import time
import serial
from avaspec import * 
import globals
import os
import matplotlib.pyplot as plt
import h5py as h5
from array import *
import ctypes
import cv2
import numpy as np
from predict import *
from robotCommands import *
from analyze import *
import csv

host = "127.0.0.1"
port = 3000

ser = serial.Serial()


test = socket.socket()
      
# print ("Socket successfully created")
# port = 3000               
# s.bind(('', port))        
# print ("socket binded to %s" %(port))
# s.listen(5)    
# print ("socket is listening")           

# while True:
#   conn, addr = s.accept()    
#   print ('Got connection from', addr )
#   with conn:
#         print(f"Connected by {addr}")
#         # conn.sendall("ack")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             # conn.sendall(data)
#             print(data)

# s.connect(('127.0.0.1', 5555))

##################################

robot_ip = '192.168.1.6'
robot_port = 3000

def positionRobot(samplePos):
    print(samplePos[0])
    print(samplePos[1])
    # robot.sendall(bytes(str(samplePos[0,0]), encoding="ascii"))

def startSpectrometer():
    ret = AVS_UseHighResAdc(globals.channel1, True)
    globals.measconfig1 = MeasConfigType()
    globals.measconfig1.m_StartPixel = 0
    globals.measconfig1.m_StopPixel = globals.pixels1 - 1
    globals.measconfig1.m_IntegrationTime = float(2)
    globals.measconfig1.m_IntegrationDelay = 0
    globals.measconfig1.m_NrAverages = int(1)
    globals.measconfig1.m_CorDynDark_m_Enable = 0  # nesting of types does NOT work!!
    globals.measconfig1.m_CorDynDark_m_ForgetPercentage = 0
    globals.measconfig1.m_Smoothing_m_SmoothPix = 0
    globals.measconfig1.m_Smoothing_m_SmoothModel = 0
    globals.measconfig1.m_SaturationDetection = 0
    globals.measconfig1.m_Trigger_m_Mode = 1
    globals.measconfig1.m_Trigger_m_Source = 0
    globals.measconfig1.m_Trigger_m_SourceType = 0
    globals.measconfig1.m_Control_m_StrobeControl = 0
    globals.measconfig1.m_Control_m_LaserDelay = 0
    globals.measconfig1.m_Control_m_LaserWidth = 0
    globals.measconfig1.m_Control_m_LaserWaveLength = 785.0
    globals.measconfig1.m_Control_m_StoreToRam = 0

    globals.measconfig2 = MeasConfigType()
    globals.measconfig2.m_StartPixel = 0
    globals.measconfig2.m_StopPixel = globals.pixels1 - 1
    globals.measconfig2.m_IntegrationTime = float(5)
    globals.measconfig2.m_IntegrationDelay = 0
    globals.measconfig2.m_NrAverages = int(1)
    globals.measconfig2.m_CorDynDark_m_Enable = 0  # nesting of types does NOT work!!
    globals.measconfig2.m_CorDynDark_m_ForgetPercentage = 0
    globals.measconfig2.m_Smoothing_m_SmoothPix = 0
    globals.measconfig2.m_Smoothing_m_SmoothModel = 0
    globals.measconfig2.m_SaturationDetection = 0
    globals.measconfig2.m_Trigger_m_Mode = 1
    globals.measconfig2.m_Trigger_m_Source = 1
    globals.measconfig2.m_Trigger_m_SourceType = 0
    globals.measconfig2.m_Control_m_StrobeControl = 0
    globals.measconfig2.m_Control_m_LaserDelay = 0
    globals.measconfig2.m_Control_m_LaserWidth = 0
    globals.measconfig2.m_Control_m_LaserWaveLength = 785.0
    globals.measconfig2.m_Control_m_StoreToRam = 0


#     AVS_SetSyncMode(globals.channel1, 1)


    
#     nummeas = globals.maxFrames

# def startSpectrometer():
#     # s.sendall(b'set_msm_name: my measurement\n')
#     globals.iris.sendall(bytes('set_msm_name: ' + globals.fileName + '\n', encoding="ascii"))
#     data = globals.iris.recv(1024)
#     # print('Recieved', data)
#     sleep(2)
#     globals.iris.sendall(b'get_msm_state\n')
#     data = globals.iris.recv(1024)
#     # print('Received', data)
#     sleep(2)
#     globals.iris.sendall(b'prepare_msm\n')
#     data = globals.iris.recv(1024)
#     # print('Received', data)
#     sleep(2)
#     globals.iris.sendall(b'get_msm_state\n')
#     data = globals.iris.recv(1024)
#     # print('Received', data)
#     sleep(2)
#     globals.iris.sendall(b'resume_msm\n')
#     data = globals.iris.recv(1024)
#     # print('Received', data)


# print("here")
# robot.connect((robot_ip, robot_port))
# 

# plt.ion()
# figure, ax = plt.subplots(figsize=(10, 8))
# line1, = ax.plot(globals.wavelength1, globals.spectraldata1)
# plt.ylim([0, 80000])
# plt.xlim([150, 1000])


def newData1():
    ret = AVS_GetScopeData(globals.channel1)
    globals.spectraldata1 = ret[1]
    # print("channel 1", globals.spectraldata1[0])

def newData2():
    ret = AVS_GetScopeData(globals.channel2)
    globals.spectraldata2 = ret[1]
    
    # print("chanel 2", globals.spectraldata2[0])
    # with h5py.File(globals.fileName + "_" + str(globals.scans) + '.h5', 'w') as f:
    #     dset = f.create_dataset("default", data = globals.spectraldata1)


    # wavelength1 = [globals.wavelength1[i] for i in range(len(globals.wavelength1))]
    # wavelength2 = [globals.wavelength2[i] for i in range(len(globals.wavelength2))]

    # spectrum1 = [globals.spectraldata1[i] for i in range(len(globals.spectraldata1))]
    # spectrum2 = [globals.spectraldata2[i] for i in range(len(globals.spectraldata2))]

    # x = np.concatenate(np.array(globals.wavelength1), np.array(globals.wavelength2))
    # y = np.concatenate(np.array(globals.spectraldata1), np.array(globals.spectraldata2))

    x1 = np.array(globals.wavelength1)
    y1 = np.array(globals.spectraldata1)
    x2 = np.array(globals.wavelength2)
    y2 = np.array(globals.spectraldata2)
    
    x = np.concatenate((x1, x2), axis=0)
    y = np.concatenate((y1, y2), axis=0)
    y = y[np.newaxis]
    if globals.scans == 1:
        # globals.spectra = y[np.newaxis]
        # print("shape", globals.spectra.shape)
        globals.wavelengths = x
        # with open("F:/LIBS/fitting3/"+globals.fileName+".csv","a", newline='') as my_csv:
        #     csvWriter = csv.writer(my_csv,delimiter=',')
        #     csvWriter.writerow(globals.wavelengths)
        #     csvWriter.writerow(y)
        with h5.File("testing/"+globals.fileName+".h5", "a") as f:
            f.create_dataset(
                name  = "wavelength",
                shape = globals.wavelengths.shape,
                data= globals.wavelengths
            )
            f.create_dataset(
                name="intensity",
                maxshape=(None, 800),
                shape=(0,800)
            )
            f["intensity"].resize((f["intensity"].shape[0] + y.shape[0]), axis = 0)
            f["intensity"][f["intensity"].shape[0]-1:] = y

    else:
        with h5.File("testing/"+globals.fileName+".h5", "a") as f:
            f["intensity"].resize((f["intensity"].shape[0] + y.shape[0]), axis = 0)
            f["intensity"][f["intensity"].shape[0]-1:] = y
        # globals.spectra = np.concatenate((globals.spectra, y[np.newaxis]), axis=0)

    # eel.map(predict(x, y))

    # print(x[5000:5005], y[5000:5005])
    # print("Channel 1", x[0], y[0])


    # figure.text(0.5,1,"Frame "+str(globals.scans))
    # line1.set_xdata(x)
    # line1.set_ydata(y)
    # figure.canvas.draw()
    # figure.canvas.flush_events()

def irisRoutine(tray,sample, name):
    globals.scan = True
    robotStopped = False

    globals.fileName = str(name)
    print("filename", globals.fileName)
    startSpectrometer()
    readyScanPosition()
    startScanMovement(sample,1)
    print(ser.read(100))
    print("PDG triggered")
    print("Scan Started**************************************")
    sleep(2)
    ser.write(b':PULSE0:STATE ON\r\n')

    data = globals.robot.recv(1)
    if data == b'1':
        ser.write(b':PULSE0:STATE OFF\r\n')
        print(ser.read(100))
        print("Scan Finished, Sample placed back")
        globals.iris.sendall(b'pause_msm\n')
        data = globals.iris.recv(1024)
        # print('Received', data)
        print("Measurement Stopped")
        analysis = analyze(globals.fileName)
        if analysis:
            eel.graph(analysis)
        else:
            eel.showModal("Analysis Failed")

def startRoutine(tray, sample, name):
    globals.scan = True
    robotStopped = False
    
    globals.fileName = str(name)
    print("filename", globals.fileName)
    
    readyScanPosition()
    startScanMovement(sample,1)
    
    sleep(2)
    # print(ser.read(100))
    print("PDG triggered")
    print("Scan Started**************************************")
    globals.spectra = np.zeros((globals.maxFrames, 8192))
    
    globals.scans = 0
    globals.scan = True
    ser.write(b':PULSE0:STATE ON\r\n')
    # ret = AVS_Measure(globals.channel2, 0, -1)
    while (globals.scan == True):
        ret = AVS_Measure(globals.channel2, 0, 1)
        ret = AVS_Measure(globals.channel1, 0, 1)
        dataready = False
        dataready2 = False
        while (dataready == False):
            dataready = (AVS_PollScan(globals.channel1) == True)
            time.sleep(0.001)
        if dataready == True:
            globals.scans = globals.scans + 1
            print("frame: " + str(globals.scans))
            newData1()
            # newData2()
        while (dataready2 == False):
            print("no data")
            dataready2 = (AVS_PollScan(globals.channel2) == True)
            time.sleep(0.001)
        if dataready2 == True:
            newData2()
        # dataready2 = (AVS_PollScan(globals.channel2) == True)
        # time.sleep(0.001)
        # if (dataready2):
        #     globals.scans = globals.scans + 1
        #     newData2()

        if (globals.scans >= globals.maxFrames):
            globals.scan = False
            ser.write(b':PULSE0:STATE OFF\r\n')
            AVS_StopMeasure(globals.channel1)
            AVS_StopMeasure(globals.channel2)
            # globals.iris.sendall(b'pause_msm\n')
            data = globals.iris.recv(1024)
            print("Measurement Stopped")
            sleep(2)
            print(ser.read(100))
            print(globals.spectra.shape)
            print(globals.wavelengths.shape)
            stopScanMovement()
            

            # convertFile("F:/LIBS/results/"+globals.fileName)
            
        
        # if dataready == True:
        #     globals.scans = globals.scans + 1
        #     if (globals.scans >= globals.maxFrames):
        #         globals.scan = False
        #         ser.write(b':PULSE0:STATE OFF\r\n')
        #         sleep(2)
        #         print(ser.read(100))
            
            
            # eel.graph(globals.wavelength1[0], globals.spectraldata1[0])
            # eel.showModal("graphing")


@eel.expose
def connectLaser():
    print(eel.EXPOSED_JS_FUNCTIONS)
    print(eel._import_js_function("graph"))
    eel.showModal("yo")

@eel.expose
def connectSpectrometer(val):
    # iris = socket.socket()
    # if (val):
    #     globals.iris.connect(('127.0.0.1', 5555))
    #     return True
    # else:
    #     globals.iris.close()
    if (val):
        if (AVS_Init(0) < 2):
            return False
        else:
            if(AVS_UpdateUSBDevices() < 2):
                return False
            mylist = AvsIdentityType()
            mylist = AVS_GetList(1)
            deviceNumbers = str(mylist[0].SerialNumber.decode("utf-8")) + " & " + str(mylist[1].SerialNumber.decode("utf-8"))
            globals.channel1 = AVS_Activate(mylist[0])
            globals.channel2 = AVS_Activate(mylist[1])
            devcon1 = DeviceConfigType()
            devcon2 = DeviceConfigType()
            devcon1 = AVS_GetParameter(globals.channel1, 63484)
            devcon2 = AVS_GetParameter(globals.channel2, 63484)
            globals.pixels1 = devcon1.m_Detector_m_NrPixels
            globals.pixels2 = devcon2.m_Detector_m_NrPixels
            globals.wavelength1 = AVS_GetLambda(globals.channel1)
            globals.wavelength2 = AVS_GetLambda(globals.channel2)
            
            
            # print("Channel 1", globals.wavelength1.size)
            # serienummer = str(mylist[0].SerialNumber.decode("utf-8"))
            
            print(deviceNumbers)
            return True
    else:
        sleep(1)
        # Need a way to deativate

@eel.expose
def connectPDG(val):
    eel.showModal("yo")
    # return True
    if val:
        # ser = serial.Serial('COM12', 115200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
        ser.port = "COM9"
        ser.baudrate = 115200
        ser.timeout = 0
        ser.parity = serial.PARITY_EVEN
        ser.rtscts = 1
        ser.open()
        if (ser.is_open):
            return True
        else:
            return False
        print("serial", ser)
    else:
        ser.close()
        if (ser.is_open):
            return False
        else:
            return True
        

@eel.expose
def connectRobot(val):
    print("here")
    if val:
        globals.robot.connect((robot_ip, robot_port))
        return True
    else:
        globals.robot.close()
        return True

@eel.expose
def showModal():    
    sleep(3)
    print("msg")
    return

@eel.expose
# def beginRoutine(name="my measurement", uvExposure = 7000, visibleExposure = 500, period = 50000, maxFrames = 50, tray=0, sample=1):
def beginRoutine(tray=0, sample=1, name="my measurement"):
    # print("exposure", float(uvExposure/1000))
    # print("exposure", float(visibleExposure/1000))
    # globals.uvExposure = uvExposure
    # positionRobot()
    
    startSpectrometer()
    globals.measconfig1.m_IntegrationTime = float(7000/1000)
    globals.measconfig2.m_IntegrationTime = float(500/1000)
    globals.maxFrames = int("100")
    globals.fileName = name
    

    ret = AVS_PrepareMeasure(globals.channel1, globals.measconfig1)
    ret = AVS_PrepareMeasure(globals.channel2, globals.measconfig2)
    print("Spectrometer Ready")
    


@eel.expose
def runAll():
    for row in range(globals.tower1.shape[0]):
        beginRoutine()
        tower1()
        setPosition(globals.tower1[row,:])
        grabSample()
        tower1(True)
        for comp in range(5):
            eel.currSample(row, comp)
            startRoutine(row+1, comp+1, globals.names[row][comp])
            
        readyScanPosition()
        tower1()
        returnTray()

@eel.expose
def runSelected(indexes):
    # print(len(indexes))
    for ind in indexes:
        beginRoutine()
        tower1()
        setPosition(globals.tower1[ind,:])
        grabSample()
        tower1(True)
        for comp in range(5):
            eel.currSample(ind, comp)
            startRoutine(ind+1, comp+1, globals.names[ind][comp])
            
        readyScanPosition()
        tower1()
        returnTray()


@eel.expose
def getFrame():
    vid = cv2.VideoCapture(1)
    res, frame = vid.read()

    if res:
        cv2.imwrite("gui/src/frame.png", frame)
        return True
    else:
        return False
    
@eel.expose
def plot(ind):
    print("graph", ind)
    plt.plot(np.array(globals.spectra)[0,:], np.array(globals.spectra)[ind+1, :])
    plt.show()

@eel.expose
def moveRobot(ind):
    positionRobot(globals.tower1[ind,:])

@eel.expose
def moveTower1():
    tower1()

@eel.expose
def gotoScanPosition():
    readyScanPosition()

@eel.expose
def lock():
    lockPiston()

@eel.expose
def release():
    openPiston()


@eel.expose
def stop():
    stopScanMovement()
    ser.write(b':PULSE0:STATE OFF\r\n')
    AVS_StopMeasure(globals.channel1)
    AVS_StopMeasure(globals.channel2)

@eel.expose
def statisticalMap():
    readyScanPosition()
    positionSample(5)
    offReturn()
    startMap()
    sleep(2)
    for i in range(30):
        for j in range(24):
            offRight()
        offDown()
        offReturn()

# eel.browsers.set_path('electron', 'gui/node_modules/electron/dist/electron')

with open("middleSample.csv", 'r', newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        globals.spectra.append([float(i) for i in row])



eel.init("gui/src", ['.tsx', '.ts', '.jsx', '.js', '.html'])


eel.start({"port": 3000}, host="localhost", port=8000)

# eel.init("front-end")
# eel.start("index.html")
# print("Started...")

# eel.init("gui/build", ['.tsx', '.ts', '.jsx', '.js', '.html'])
# eel.start('index.html')
