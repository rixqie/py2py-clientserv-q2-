# import the socket library
import socket

# create a socket object
s = socket.socket()
print ("Socket successfully created")
#reserve a port
port = 8080
# bind to the port
s.bind(('', port))
# print the output
print ("socket binded to %s" %(port))
# put the socket into listening mode
s.listen(5)
print ("socket is listening")
# a forever loop
c, addr = s.accept()
while True:
# receive data stream no greater than 1024 bytes
 data = c.recv(1024).decode("ascii")
 if not data:
  # if data is not received break
   break
        #print("from connected user: " + str(data))
 data = "\nFrom server xyz: " + str(data) +"\n"
 c.send(data.encode())  # send data to the client
c.close()  # close the connection
#Establish connection with client.
