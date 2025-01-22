import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1099))
client.sendall(b"Hello, This is Client!")
