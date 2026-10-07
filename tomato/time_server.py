import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"      
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("UDP Time Server is running...")
print(f"Listening on {HOST}:{PORT}")

def handle_request(data, client_address):
    """Handle each client request."""
    print(f"Request received from {client_address}")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    server.sendto(current_time.encode(), client_address)

while True:
    data, client_address = server.recvfrom(1024)

    thread = threading.Thread(target=handle_request,
                              args=(data, client_address))
    thread.start()