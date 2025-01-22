import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1099))
server.listen(1)
print("Waiting for connection...")
conn, addr = server.accept()
print("Connected by:", addr)
message = conn.recv(1024)
print("Client says:", message.decode())
conn.close()
