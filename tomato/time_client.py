import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "TIME"

client.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

time_data, server = client.recvfrom(1024)

print("Current Server Time:")
print(time_data.decode())

client.close()