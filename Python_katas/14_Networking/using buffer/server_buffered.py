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
    
    buffer = b""  # Receive buffer
    BUFFER_SIZE = 1024
    
    while True:
        # Receive data into buffer
        chunk = client.recv(BUFFER_SIZE)
        if not chunk:
            break
        
        buffer += chunk
        
        # Process complete messages (assuming messages end with \\n)
        while b'\\n' in buffer:
            message, buffer = buffer.split(b'\\n', 1)
            msg_text = message.decode()
            print(f"Client: {msg_text}")
            
            # Send response
            response = input("Server: ") + "\\n"
            client.send(response.encode())
    
    client.close()
    print("Client disconnected")
