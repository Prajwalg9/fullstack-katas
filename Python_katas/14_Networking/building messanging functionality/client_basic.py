import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))
print("Connected to server. Type 'quit' to exit.")

while True:
    message = input("You: ")
    s.send(message.encode())
    
    if message.lower() == 'quit':
        break
    
    data = s.recv(1024).decode()
    print(f"Server: {data}")

s.close()
