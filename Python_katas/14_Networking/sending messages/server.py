import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)
print(f"Server listening on {HOST_NAME}:{PORT}")

while True:
    client, address = s.accept()
    print(f"Client connected from {address}")
    
    while True:
        # Receive message from client
        data = client.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")
        
        # Send response back
        message = input("Server: ")
        client.send(message.encode())
    
    client.close()
    print("Client disconnected")
