import socket
import eel
from time import sleep
import time
import serial
import winsound
import globals

robot = socket.socket() 

robot_ip = '192.168.1.6'
robot_port = 3000

robot.connect((robot_ip, robot_port))

sleep(2)


def positionRobot(samplePos):
    print("height:", samplePos[0])
    print("in:", samplePos[1])
    print("up:", samplePos[2])
    robot.sendall(bytes(str(samplePos[0]), encoding="ascii"))
    positioned = False
    while not positioned:
        data = robot.recv(1)
        if data == b'1':
            robot.sendall(bytes(str(samplePos[1]), encoding="ascii"))
        elif data == b'2':
            robot.sendall(bytes(str(samplePos[2]), encoding="ascii"))
        elif data == b'3':
            break

# while True:
#     tray = input("Enter Tray position: ")
#     tray = tray.split(",")
#     tray = [float(i) for i in tray]
#     positionRobot(tray)
# for i in range(globals.tower1.shape[0]):
#     positionRobot(globals.tower1[i,:])
positionRobot(globals.tower1[2,:])