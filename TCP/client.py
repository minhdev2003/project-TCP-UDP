import socket

TCP_IP = '127.0.0.1'  # Local loopback address
TCP_PORT = 5005
BUFFER_SIZE = 20
MESSAGE = "Hello, Server!"

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((TCP_IP, TCP_PORT))

# Send the message
s.send(MESSAGE.encode())  # Encode string to bytes before sending

# Receive the response (echoed back from the server)
data = s.recv(BUFFER_SIZE)
print("received data:", data.decode())  # Decode bytes to string for printing

# Close the connection
s.close()
