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
    c.send(bytes('A command issued in server side: to be executed in client side', 'utf-8'))
    c.close()