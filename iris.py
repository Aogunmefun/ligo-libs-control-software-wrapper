import socket
import eel
from time import sleep
import time
import serial
import winsound

host = "127.0.0.1"
port = 3000
ser = serial.Serial('COM9', 115200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

robot = socket.socket() 
iris = socket.socket()

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
# robot_ip = '192.168.1.6'
# robot_port = 3000
# s.connect((robot_ip, robot_port))
# s.sendall(b'1')
################################

robot_ip = '192.168.1.6'
robot_port = 3000

def startSpectrometer(name):
    # s.sendall(b'set_msm_name: my measurement\n')
    iris.sendall(bytes('set_msm_name: ' + name + '\n', encoding="ascii"))
    data = iris.recv(1024)
    print('Recieved', data)
    sleep(2)
    iris.sendall(b'get_msm_state\n')
    data = iris.recv(1024)
    print('Received', data)
    sleep(2)
    iris.sendall(b'prepare_msm\n')
    data = iris.recv(1024)
    print('Received', data)
    sleep(2)
    iris.sendall(b'get_msm_state\n')
    data = iris.recv(1024)
    print('Received', data)
    sleep(2)
    iris.sendall(b'resume_msm\n')
    data = iris.recv(1024)
    print('Received', data)
    # iris.close()




@eel.expose
def showModal(msg):
    print(msg)

@eel.expose
def start_routine():
    print("here")
    robot.connect((robot_ip, robot_port))
    robot.sendall(b'1')



# eel.init('gui/client')
# eel.start({"port": 3000}, host="localhost", port=8888)
# print("Started...")

# eel.init("gui/build")
# eel.start('index.html')

# print("here")
# robot.connect((robot_ip, robot_port))
# 

def startRoutine(name, offset, distance):
    count = 0
    robot.sendall(bytes(str(offset), encoding="ascii"))
    while True:
        data = robot.recv(1)
        print('Received', data)
        if (data==b'4'):
            sleep(3)
            print("In position For scan")
            startSpectrometer(name)
            print("Spectrometer Ready")
            # robot.sendall(bytes(str(distance), encoding="ascii")) ######## measurement distance
            # robot.sendall(bytes(str(speed), encoding="ascii")) ######## speed (seconds between sample movements)
            # robot.sendall(b'1')
            # robot.sendall(bytes(str(32), encoding="ascii"))
            robot.sendall(bytes(str(15), encoding="ascii"))
            ser.write(b':PULSE0:STATE ON\r\n')
            print("PDG triggered")
            sleep(2)
            print(ser.read(100))
            
            print("Scan Started")
        elif (data==b'3'):
            robot.sendall(bytes(str(distance), encoding="ascii"))
            # s.close()
        elif (data==b'5'):
            ser.write(b':PULSE0:STATE OFF\r\n')
            sleep(2)
            print(ser.read(100))
            print("Scan Finished, Sample placed back")
            iris.sendall(b'pause_msm\n')
            data = iris.recv(1024)
            print('Received', data)
            print("Measurement Stopped")
            # iris.close()
            # robot.close()
            break

# iris.connect(('127.0.0.1', 5555))
# # iris.sendall(b'set_msm_name: my measurement\n')
# iris.sendall(bytes('set_msm_name: my measurement\n', encoding="ascii"))
# data = iris.recv(1024)
# print('Recieved', data)

iris.connect(('127.0.0.1', 5555))
robot.connect((robot_ip, robot_port))

uVExposure = 7000
visibleExposure = 700

z = 23.5

# sleep(0.1)
# winsound.Beep(frequency, duration)

# while (1):
#     a = float(input("Distance: "))
#     print(a)
#     startRoutine(name = "19003314550_Tray3_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure)+"_"+str(a)+"cm", distance = -((a-20)*10), offset = -10)

startRoutine(name = "17001284", distance = -((z-20)*10), offset = 90)
sleep(2)
startRoutine(name = "17001335", distance = -((z-20)*10), offset = 52)
sleep(2)
startRoutine(name = "17001282"+"_"+str(z)+"cm", distance = -((z-20)*10), offset = 14)
# startRoutine(name = "18502158550_Tray3", speed = 3, distance = -140)
# sleep(2)
# startRoutine(name = "10501789150"+"_"+str(z)+"cm", distance = -((z-20)*10), offset = -24)

# for i in range(1,21):
#     startRoutine(name = "18502084550_Tray1_"+str(20+i)+"cm", distance = -10*i, offset = -75)
#     sleep(2)
#     startRoutine(name = "19003762550_Tray2_"+str(20+i)+"cm", distance = -10*i, offset = -50)
#     sleep(2)
#     startRoutine(name = "19003314550_Tray3_"+str(20+i)+"cm", distance = -10*i, offset = -10)
#     # startRoutine(name = "18502158550_Tray3", speed = 3, distance = -140)
#     sleep(2)
#     startRoutine(name = "10501746150_Tray4_"+str(20+i)+"cm", distance = -10*i, offset = 30)
#     frequency = 300  # Set Frequency To 2500 Hertz
#     duration = 1000  # Set Duration To 1000 ms == 1 second
#     winsound.Beep(frequency, duration)
#     input("Press Enter when ready")
# sleep(2)
# startRoutine(name = "10501789150_Tray5", speed = 3, distance = -180)
# startRoutine(name = "1050_1676_150-prt1", speed = 3, distance = 85)
# sleep(2)
# startRoutine(name = "1050_1676_150-prt2", speed = 3, distance = 50)
# sleep(2)
# startRoutine(name = "1900_3630_550-prt1", speed = 3, distance = -30)
# sleep(2)
# startRoutine(name = "1900_3630_550-prt2", speed = 3, distance = -65)




# input("Press enter when you're ready to continue scan")
# startRoutine(name = "speed_fast_distance_"+str(0)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 3, distance = 0)
# input("Press enter when you're ready to continue scan")
# startRoutine(name = "speed_fast_distance_"+str(0)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 3, distance = 0)

# For each speed (fast, medium, slow) I'm testing different distances (+-10mm)

# for i in range(5):
#     print("Starting Routine...")
#     startRoutine(name = "speed_fast_distance_"+str(i)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 3, distance = i)
#     sleep(5)

# for i in range (5):
#     print("Starting Routine...")
#     startRoutine(name = "speed_medium_distance_"+str(i)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 2, distance = i)
#     sleep(5)

# for i in range (5):
#     print("Starting Routine...")
#     start = time.time()
#     startRoutine(name = "speed_slow_distance_"+str(i)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 1, distance = i)
#     end = time.time()
#     print("Time Passed", end - start)
#     sleep(5)


# # Negative Distances

# for i in range(5):
#     print("Starting Routine...")
#     startRoutine(name = "speed_fast_distance_-"+str(i)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 3, distance = -i)
#     sleep(5)

# for i in range (5):
#     print("Starting Routine...")
#     startRoutine(name = "speed_medium_distance_-"+str(i)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 2, distance = -i)
#     sleep(5)

# for i in range (5):
#     print("Starting Routine...")
#     startRoutine(name = "speed_slow_distance_-"+str(i)+"_exposureUV_"+str(uVExposure)+"_exposureVisible_"+str(visibleExposure), speed = 1, distance = -i)
#     sleep(5)



####### Add more of buffer for laser shots at the end of routine

# ser.write(b':PULSE0:STATE OFF\r\n')
# ser.write(b':PULSE0:WIDTH?\r\n')
# sleep(2)
# print(ser.read(100))