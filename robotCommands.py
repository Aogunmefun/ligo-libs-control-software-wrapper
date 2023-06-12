import socket
import eel
from time import sleep
import time
import serial
import winsound
import globals
import csv


robot = globals.robot
# robot = socket.socket() 

# robot_ip = '192.168.1.6'
# robot_port = 3000

# robot.connect((robot_ip, robot_port))

# sleep(2)


def setPosition(pos):
    robot.sendall(bytes(str(0), encoding="ascii"))
    stored = False
    while not stored:
        data = robot.recv(1)
        if data == b'0':
            print("Mode recieved")
            sleep(2)
            robot.sendall(bytes(str(pos[0]), encoding="ascii"))
        if data == b'1':
            print("Got Height")
            robot.sendall(bytes(str(pos[1]), encoding="ascii"))
        elif data == b'2':
            print("Got in distance")
            robot.sendall(bytes(str(pos[2]), encoding="ascii"))
        elif data == b'3':
            print("Got up distance")
            # break
            stored = True

def grabSample():
    robot.sendall(bytes(str(5), encoding="ascii"))
    returned = False
    while not returned:
        data = robot.recv(1)
        if data == b'0':
            print("Mode Received")
            
        elif data == b'1':
            print("Sample Obtained")
            returned = True

def positionRobot(samplePos):
    print("height:", samplePos[0])
    print("in:", samplePos[1])
    print("up:", samplePos[2])
    robot.sendall(bytes(str(samplePos[0]), encoding="ascii"))
    positioned = False
    while not positioned:
        data = robot.recv(1)
        if data == b'0':
            print("Mode received")
        if data == b'1':
            robot.sendall(bytes(str(samplePos[1]), encoding="ascii"))
        elif data == b'2':
            robot.sendall(bytes(str(samplePos[2]), encoding="ascii"))
        elif data == b'3':
            # break
            continue
        elif data == b'4':
            positioned = True

def returnTray():
    robot.sendall(bytes(str(4), encoding="ascii"))
    returned = False
    while not returned:
        data = robot.recv(1)
        if data == b'0':
            print("Mode Received")
            
        elif data == b'1':
            print("Sample returned")
            returned = True

def tower1(linear = False):
    if not linear:
        robot.sendall(bytes(str(1), encoding="ascii"))
    else:
        robot.sendall(bytes(str(9), encoding="ascii"))
    done = False
    while not done:
        data = robot.recv(1)
        if data == b'0':
            print("Mode Received")
            
        elif data == b'1':
            print("In front of Tower 1")
            done = True

def readyScanPosition():
    robot.sendall(bytes(str(3), encoding="ascii"))
    done = False
    while not done:
        data = robot.recv(1)
        if data == b'0':
            print("Mode Received")
            
        elif data == b'1':
            print("Ready to scan")
            done = True


def positionSample(pos):
    robot.sendall(bytes(str(11), encoding="ascii"))
    moved = False
    while not moved:
        data = robot.recv(1)
        if data == b'0':
            robot.sendall(bytes(str(90-((5-pos)*38)), encoding="ascii"))
            print("Mode Received")
        elif data == b'1':
            robot.sendall(bytes(str(0), encoding="ascii"))
            print("Recived horizontal offset")
        elif data == b'2':
            print("Recived vertical offset")
        elif data == b'3':
            print("Gone to Position")
            moved = True

def startScanMovement(pos, passes):
    robot.sendall(bytes(str(8), encoding="ascii"))
    done = False
    while not done:
        data = robot.recv(1)
        if data == b'0':
            robot.sendall(bytes(str(90-((5-pos)*38)), encoding="ascii"))
            print("Mode Received")
        elif data == b'1':
            robot.sendall(bytes(str(0), encoding="ascii"))
            print("Recived horizontal offset")
        elif data == b'2':
            robot.sendall(bytes(str(0), encoding="ascii"))
            print("Recived vertical offset")
        elif data == b'3':
            print("Received number of passes")
            done = True

def stopScanMovement():
    robot.sendall(bytes(str(0), encoding="ascii"))
    stopped = False
    while not stopped:
        data = robot.recv(1)
        if data == b'0':
            print("scan Stopped")
            stopped = True
            # robot.sendall(bytes(str(8), encoding="ascii"))

def lockPiston():
    robot.sendall(bytes(str(6), encoding="ascii"))
    locked = False
    while not locked:
        data = robot.recv(1)
        if data == b'0':
            print("scan Stopped")
            locked = True

def openPiston():
    robot.sendall(bytes(str(7), encoding="ascii"))
    open = False
    while not open:
        data = robot.recv(1)
        if data == b'0':
            print("scan Stopped")
            open = True

def startMap():
    robot.sendall(bytes(str(10), encoding="ascii"))
    res = False
    while not res:
        data = robot.recv(1)
        if data == b'0':
            print("Mapping Mode Selected")
            res = True

def offRight():
    robot.sendall(bytes(str(4), encoding="ascii"))
    res = False
    while not res:
        data = robot.recv(1)
        if data == b'0':
            print("Moved Right")
            res = True

def offReturn():
    robot.sendall(bytes(str(2), encoding="ascii"))
    res = False
    while not res:
        data = robot.recv(1)
        if data == b'0':
            print("Return to start")
            res = True

def offDown():
    robot.sendall(bytes(str(3), encoding="ascii"))
    res = False
    while not res:
        data = robot.recv(1)
        if data == b'0':
            print("Moved Down")
            res = True

def stopMap():
    robot.sendall(bytes(str(1), encoding="ascii"))
    res = False
    while not res:
        data = robot.recv(1)
        if data == b'0':
            print("Stopped Map")
            res = True
# globals.fileName = globals.names[0][0]

# with open("F:/LIBS/results"+str(globals.fileName)+".csv","w+", newline='') as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerow(globals.wavelengths)
#     csvWriter.writerows(globals.spectra)

# def setMode(mode):
#     robot.sendall(bytes(str(mode), encoding="ascii"))
#     resp = False
#     while not resp:
#         data = robot.recv(1)
#         if 

# while True:
#     tray = input("Enter Tray position: ")
#     tray = tray.split(",")
#     tray = [float(i) for i in tray]
#     positionRobot(tray)
# for i in range(globals.tower1.shape[0]):
#     positionRobot(globals.tower1[i,:])
# positionRobot(globals.tower1[2,:])

# setPosition(globals.tower1[2,:])


# for row in range(globals.tower1.shape[0]):
# # for row in range(8,10):
#     tower1()
#     setPosition(globals.tower1[row,:])
#     grabSample()
    # tower1(True)
    # readyScanPosition()
    # tower1()
    # returnTray()
# tower1()
# setPosition(globals.tower1[0,:])
# grabSample()
# tower1()
# setPosition(globals.tower1[2,:])
# grabSample()
# tower1()
# readyScanPosition()
# startScanMovement(1,1)
# sleep(5)
# stopScanMovement()
# tower1()
# returnTray()