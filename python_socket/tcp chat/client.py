import socket 
def Main():
        host = '127.0.0.1'
        port = 5000
        mySocket = socket.socket()
        mySocket.connect((host,port))
        print("Enter 'q' to terminate connection")     
        message =input(" Client :  ")
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                print ('Server : ' + data)
                message = input(" Client :  ")
        mySocket.close()
if __name__ == '__main__':
    Main()