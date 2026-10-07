import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sentence = input("Enter a new sentence:\n ")

client.sendto(sentence.encode(), (HOST,PORT))
translated,_  = client.recvfrom(2048)

print("\nTranslated sentence: "+translated.decode())
client.close()