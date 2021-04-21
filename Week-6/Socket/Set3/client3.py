import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Client socket created')

c.connect(('localhost', 9999))

mssg = input('Enter your message: ')
c.send(bytes(mssg, 'utf-8'))

print(c.recv(1024).decode())