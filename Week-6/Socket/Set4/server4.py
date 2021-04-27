import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234




## CREATE A SERVER SOCKET ##
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, so server informs operating system that it's going to use given IP and port
# For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.bind((IP, PORT))

# This makes server listen to new connections
server_socket.listen()
print(f'Listening for connections on {IP}:{PORT}...')




## HANDLE RECEIVING MESSAGES ##
def receive_message(client_socket):
    try:
        # Receive our "datalen" containing message length, it's size is defined and constant
        mssgLength = client_socket.recv(HEADER_LENGTH)
        # If we received no data, client gracefully closes a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(mssgLength):
            return False
        # Convert datalen to int value
        mssgLengthInt = int(mssgLength.decode('utf-8').strip()) #message_length
        # Return an object of message datalen and message data
        return {'datalen': mssgLength.decode('utf-8'), 'data': client_socket.recv(mssgLengthInt).decode('utf-8')}
    except:
        # If we are here, client closed connection violently, for example by pressing ctrl+c on his script or just lost his connection
        # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write) and that's also a cause when we receive an empty message
        return False




# List of sockets for select.select()
sockets_list = [server_socket]
# List of connected clients: socket as a key, {datalen, data} as value
clients = {}


while True:

    # Calls Unix select() system call or Windows select() WinSock call with three parameters:
    #   - rlist - sockets to be monitored for incoming data
    #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
    #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
    # Returns lists:
    #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
    #   - writing - sockets ready for data to be send thru them
    #   - errors  - sockets with some exceptions
    # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    
    # print('read_sockets', read_sockets)
    # print('exception_sockets', exception_sockets)
    # print('server_socket', server_socket)
    



    # Iterate over notified sockets
    for notified_socket in read_sockets:

        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:

            # Accept new connection
            # Returns a new socket - client socket, connected to this given client only, it's unique for that client
            # The other returned object is (ip,port) set
            client_socket, client_address = server_socket.accept()

            # Client should send his name right away, receive it
            user = receive_message(client_socket)

            # If False - client disconnected before he sent his name
            if user is False:
                continue

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)
            # Also save username and datalen
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data']))



        # Else existing socket is sending a message
        else:

            # Receive message
            message = receive_message(notified_socket)


            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data']))

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)
                # Remove from our list of users
                del clients[notified_socket]

                continue


            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]
            print(f'Received message from {user["data"]}: {message["data"]}')


            # Iterate over connected clients and broadcast message
            for client_socket in clients:
                # But don't sent it to sender
                if client_socket != notified_socket:
                    # Send user and message (both with their datalen)
                    client_socket.send(bytes(user['datalen'] + user['data'] + message['datalen'] + message['data']))



    # It's not really necessary to have this, but will handle (by deleting) some socket exceptions just in case
    for notified_socket in exception_sockets:
        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)
        # Remove from our list of users
        del clients[notified_socket]