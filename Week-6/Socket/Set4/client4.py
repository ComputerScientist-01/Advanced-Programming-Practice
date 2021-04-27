import socket
import select
import errno
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234




my_username = input("Username: ")




## CREATE A CLIENT SOCKET ##
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## CONNECT TO GIVEN IP & PORT ##
client_socket.connect((IP, PORT))
# .recv() call won't block, instead will just return some exception that we'll handle
client_socket.setblocking(False)




# Prepare username and usernameLength and send them to the server
username = my_username.encode('utf-8')
usernameLength = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(usernameLength + username)




while True:

    # Wait for user to input a message
    message = input(f'{my_username} > ')

    # If message is not empty -> send it
    if message:
        message = message.encode('utf-8')
        messageLength = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(messageLength + message)



    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "usernameLength", it's size is defined and constant
            usernameLength = client_socket.recv(HEADER_LENGTH)
            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(usernameLength):
                print('Connection closed by the server')
                sys.exit()
            # Convert usernameLength to int value
            usernameLengthInt = int(usernameLength.decode('utf-8').strip())
            # Receive and decode username
            username = client_socket.recv(usernameLengthInt).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            messageLength = client_socket.recv(HEADER_LENGTH)
            messageLengthInt = int(messageLength.decode('utf-8').strip())
            message = client_socket.recv(messageLengthInt).decode('utf-8')

            # Print message
            print(f'{username} > {message}')



    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        # We just did not receive anything
        continue



    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: {}'.format(str(e)))
        sys.exit()