import socket

TCP_IP = '127.0.0.1'  
TCP_PORT = 5005
BUFFER_SIZE = 20

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
s.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
s.listen(1)

print("Server is waiting for a connection...")
conn, addr = s.accept()

print('Connection address:', addr)

# Start receiving data from the client
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("received data:", data.decode())  # Decode bytes to string for printing
    conn.send(data)  # Echo the received data back to the client

# Close the connection
conn.close()
