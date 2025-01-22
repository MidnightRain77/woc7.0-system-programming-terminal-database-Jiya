import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1099))
server.listen(1)
print("Waiting for connection...")
conn, addr = server.accept()
print("Connected by:", addr)
conn.sendall(b"Hello, Client!")
conn.close()
