import socket
 
def Main():
    host = "127.0.0.1"
    port = 5000
    data=list() 
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            d = conn.recv(1024).decode()
            print("Client message:",d)
            data.append(d)
            if not d:
                    break
            #print("Client : ",d)
            if d :
                ack = '1'
            else:
                ack = '0'
            conn.send(ack.encode())
    print(data)         
    conn.close()
     
if __name__ == '__main__':
    Main()
