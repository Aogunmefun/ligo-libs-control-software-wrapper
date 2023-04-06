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

host = "127.0.0.1"
port = 3000

ser = serial.Serial()


robot = socket.socket() 
iris = socket.socket()
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


def startSpectrometer(name):
    ret = AVS_UseHighResAdc(globals.channel1, True)
    measconfig = MeasConfigType()
    measconfig.m_StartPixel = 0
    measconfig.m_StopPixel = globals.pixels - 1
    measconfig.m_IntegrationTime = float(2)
    measconfig.m_IntegrationDelay = 0
    measconfig.m_NrAverages = int(1)
    measconfig.m_CorDynDark_m_Enable = 0  # nesting of types does NOT work!!
    measconfig.m_CorDynDark_m_ForgetPercentage = 0
    measconfig.m_Smoothing_m_SmoothPix = 0
    measconfig.m_Smoothing_m_SmoothModel = 0
    measconfig.m_SaturationDetection = 0
    measconfig.m_Trigger_m_Mode = 1
    measconfig.m_Trigger_m_Source = 0
    measconfig.m_Trigger_m_SourceType = 0
    measconfig.m_Control_m_StrobeControl = 0
    measconfig.m_Control_m_LaserDelay = 0
    measconfig.m_Control_m_LaserWidth = 0
    measconfig.m_Control_m_LaserWaveLength = 785.0
    measconfig.m_Control_m_StoreToRam = 0
    ret = AVS_PrepareMeasure(globals.channel1, measconfig)
    nummeas = globals.maxFrames


# print("here")
# robot.connect((robot_ip, robot_port))
# 



def startRoutine(name, speed, distance):
    # robot.sendall(b'1')
    globals.scan = True
    while globals.scan:
        # data = robot.recv(1024)
        # print('Received', data)
        data=b'3'
        if (data==b'3'):
            sleep(3)
            print("In position For scan")
            startSpectrometer(name)
            print("Spectrometer Ready")
            robot.sendall(bytes(str(distance), encoding="ascii")) ######## measurement distance
            ser.write(b':PULSE0:STATE ON\r\n')
            sleep(2)
            print(ser.read(100))
            print("PDG triggered")
            print("Scan Started")
            plt.ion()
            figure, ax = plt.subplots(figsize=(10, 8))
            line1, = ax.plot(globals.wavelength1, globals.spectraldata1)
            plt.ylim([0, 10000])
            scans = 0
            globals.scan = True
            while (globals.scan == True):
                ret = AVS_Measure(globals.channel1, 0, 1)
                dataready = False
                while (dataready == False):
                    dataready = (AVS_PollScan(globals.channel1) == True)
                    time.sleep(0.001)
                if dataready == True:
                    scans = scans + 1
                    if (scans >= globals.maxFrames):
                        globals.scan = False
                        ser.write(b':PULSE0:STATE OFF\r\n')
                        sleep(2)
                        print(ser.read(100))
                    ret = AVS_GetScopeData(globals.channel1)
                    timestamp = ret[0]
                    globals.spectraldata1 = ret[1]
                    print("data", globals.spectraldata1[0])
                    figure.text(0.5,1,"Frame "+str(scans))
                    line1.set_xdata(globals.wavelength1)
                    line1.set_ydata(globals.spectraldata1)
                    figure.canvas.draw()
                    figure.canvas.flush_events()
                    sleep(0.001)
                        
                sleep(0.001)
            plt.close(figure) 
            # s.close()
        elif (data==b'4'):
            ser.write(b':PULSE0:STATE OFF\r\n')
            sleep(2)
            print(ser.read(100))
            print("Scan Finished, Sample placed back")
            # iris.sendall(b'pause_msm\n')
            # data = iris.recv(1024)
            # print('Received', data)
            AVS_StopMeasure(globals.channel1)
            AVS_StopMeasure(globals.channel2)
            print("Measurement Stopped")
            # iris.close()
            # robot.close()
            break


@eel.expose
def connectSpectrometer(val):
    # iris = socket.socket()
    # if (val):
    #     iris.connect(('127.0.0.1', 5555))
    # else:
    #     iris.close()
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
            globals.pixels = devcon1.m_Detector_m_NrPixels
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
    # return True
    if val:
        # ser = serial.Serial('COM12', 115200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
        ser.port = "COM12"
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
    if val:
        robot.connect((robot_ip, robot_port))
        return True
    else:
        robot.close()
        return True

@eel.expose
def showModal():    
    sleep(3)
    print("msg")
    return

@eel.expose
def beginRoutine(name="my measurement", uvExposure = 1, visibleExposure = 10, period = 50000, maxFrames = 500):
    print("exposure", float(uvExposure))
    startRoutine(name = name, speed = 3, distance = 0)


# eel.browsers.set_path('electron', 'gui/node_modules/electron/dist/electron')



eel.init('client')
eel.start({"port": 3000}, host="localhost", port=8000)
# eel.start("localhost:3000/index.html", host="localhost", port=8000)

# eel.init("front-end")
# eel.start("index.html")
# print("Started...")

# eel.init("gui/build")
# eel.start('index.html')