import socket
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

class ServerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Server")
        self.root.geometry("400x500")
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self.root, state='disabled')
        self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Message entry
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5, padx=10, fill=tk.X)
        self.entry.bind('<Return>', self.send_message)
        
        # Send button
        send_btn = tk.Button(self.root, text="Send", command=self.send_message)
        send_btn.pack(pady=5)
        
        self.client = None
        self.start_server()
        
    def log(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + '\\n')
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def start_server(self):
        Thread(target=self.server_loop, daemon=True).start()
    
    def server_loop(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = socket.gethostname()
        PORT = 12345
        
        s.bind((HOST, PORT))
        s.listen()
        self.log(f"Server listening on {HOST}:{PORT}")
        
        self.client, addr = s.accept()
        self.log(f"Client {addr} connected")
        
        Thread(target=self.receive_messages, daemon=True).start()
    
    def receive_messages(self):
        while True:
            try:
                data = self.client.recv(1024).decode()
                if data:
                    self.log(f"Client: {data}")
            except:
                self.log("Client disconnected")
                break
    
    def send_message(self, event=None):
        message = self.entry.get()
        if message and self.client:
            self.client.send(message.encode())
            self.log(f"You: {message}")
            self.entry.delete(0, tk.END)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ServerGUI()
    app.run()
