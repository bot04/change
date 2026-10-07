import pickle
import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)
print("server is waiting for a connection...")
conn, addr = server.accept()
print(f"connected by {addr}")
data = conn.recv(4096)
matrix = pickle.loads(data)
n = len(matrix)

upper = True
lower = True
diagonal = True

for i in range(n):
    for j in range(n):
        if i > j and matrix[i][j] != 0:
            upper = False
        if i < j and matrix[i][j] != 0:
            lower = False
        if i != j and matrix[i][j] != 0:
            diagonal = False

if diagonal:
    matrix_type = "diagonal matrix"
elif upper:
    matrix_type = "upper triangular matrix"
elif lower:
    matrix_type = "lower triangular matrix"
else:
    matrix_type = "neither upper triangular,lower triangular,nor diagonal"

conn.send(matrix_type.encode())
conn.close()

server.close()