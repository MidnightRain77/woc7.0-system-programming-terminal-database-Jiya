import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1099))
message = client.recv(1024)
print("Server says:", message.decode())
