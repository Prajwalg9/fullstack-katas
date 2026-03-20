import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))
print(f"Connected to server {HOST_NAME}:{PORT}")

while True:
    # Send message to server
    message = input("Client: ")
    s.send(message.encode())
    
    # Receive response from server
    data = s.recv(1024).decode()
    if not data:
        break
    print(f"Server: {data}")

s.close()
