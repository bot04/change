import pickle
import random
import socket

HOST = "127.0.0.1"
PORT = 5000

n = int(input("Enter the order of the matrix(n):"))
matrix = [[random.randint(1, 50) for i in range(n)] for i in range(n)]
print("\nGenerated Matrix")
for row in matrix:
    print(row)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(pickle.dumps(matrix))
result = client.recv(1024).decode()
print("\nMatrix Type:", result)
client.close()