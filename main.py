import socket

host = "127.0.0.1"
port = 3000

s = socket.socket()        
print ("Socket successfully created")
port = 3000               
s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen(5)    
print ("socket is listening")           

while True:
  conn, addr = s.accept()    
  print ('Got connection from', addr )
  with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # conn.sendall(data)
            print(data)
#   c.send('Thank you for connecting'.encode())
#   c.close()
#   break