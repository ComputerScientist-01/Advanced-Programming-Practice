import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created!')

# RANGE FOR PORT NUMBER: 0 - 65535
s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connections')

while True:
    c, c_addr = s.accept()
    print('Connected with ', c_addr)
    mssg = c.recv(1024).decode()
    if mssg == 'PING':
        print('PONG')
    else:
        pass
    c.close()