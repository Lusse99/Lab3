# Import socket module
from socket import *    

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 80

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
        print('Waiting for requests ...')
        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
                message =  connectionSocket.recv(1024)
                # -------------------------------------------
                #       Request handling Section
                # -------------------------------------------
                data_received=message.split(b'\r\n')
                for line in data_received:
                    print(line.decode("utf-8"))

                request_line = data_received[0].decode("utf-8")
                request_components = request_line.split(" ")
                requested_resource = request_components[1]
                f = open(requested_resource[1:],"rb")
                outputdata = f.read()
                
                header = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
                connectionSocket.send(header)
        
                connectionSocket.sendall(outputdata)
                print(f"Requested resource: {requested_resource}")
                
        except IOError:
                # ----------------------------------
                #       I/O Error handling
                # ----------------------------------
                        connectionSocket.close()
        except IndexError:
                print('Index error exception')                          
serverSocket.close()                
                
                
        

