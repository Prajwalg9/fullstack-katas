import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen()
print(f"Server started on {HOST_NAME}:{PORT}")

client, address = s.accept()
print(f"Client {address} connected")

while True:
    data = client.recv(1024).decode()
    if data.lower() == 'quit':
        break
    
    print(f"Client: {data}")
    response = input("Server: ")
    client.send(response.encode())

client.close()
s.close()
