import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))
print(f"Connected to server {HOST_NAME}:{PORT}")

BUFFER_SIZE = 1024

while True:
    message = input("Client: ") + "\\n"
    
    # Send message
    total_sent = 0
    message_bytes = message.encode()
    
    while total_sent < len(message_bytes):
        sent = s.send(message_bytes[total_sent:])
        total_sent += sent
    
    # Receive response with buffer
    buffer = b""
    while b'\\n' not in buffer:
        chunk = s.recv(BUFFER_SIZE)
        if not chunk:
            break
        buffer += chunk
    
    if b'\\n' in buffer:
        response, _ = buffer.split(b'\\n', 1)
        print(f"Server: {response.decode()}")

s.close()
