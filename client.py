# Import socket module
import socket
# Create a socket object
s = socket.socket()
# Define the server's ip address and port
s.connect(('127.0.0.1', 8080))
message = input("Enter message: ")  # take input
s.send(message.encode())  # send message
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()
