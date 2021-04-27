import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Client socket created')

c.connect(('localhost', 9999))

print(c.recv(1024).decode())