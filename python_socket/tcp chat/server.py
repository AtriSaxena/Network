import socket 
def Main():
    host = "127.0.0.1"
    port = 5000
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("Client : " + str(data))
            data = input("Server :  ")
            conn.send(data.encode())
    conn.close()
if __name__ == '__main__':
    Main()