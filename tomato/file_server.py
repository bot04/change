import socket
import threading
import os

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(5)

print("File Server is running...")
print(f"Listening on {HOST}:{PORT}")

def handle_client(client_socket, address):
    print(f"Connected to {address}")

    try:
        filename = client_socket.recv(1024).decode()

        pid = os.getpid()

        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()

            response = f"SERVER PID: {pid}\n\nFile Content:\n{content}"
        else:
            response = f"SERVER PID: {pid}\n\nError: File '{filename}' not found."

        client_socket.send(response.encode())

    except Exception as e:
        print("Error:", e)

    finally:
        client_socket.close()
        print(f"Connection closed with {address}")

while True:
    client_socket, address = server.accept()

    thread = threading.Thread(target=handle_client,
                              args=(client_socket, address))
    thread.start()