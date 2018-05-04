def rolling_window(seq, window_size):
    it = iter(seq)
    win = [next(it) for cnt in range(window_size)] # First window
    yield win
    for e in it: # Subsequent windows
        win[:-1] = win[1:]
        win[-1] = e
        yield win

if __name__=="__main__":
    for w in rolling_window(range(6), 3):
        print(w)

import socket 
def Main():
        host = '127.0.0.1'
        port = 5000
        mySocket = socket.socket()
        mySocket.connect((host,port))
        window_size = 3
        seq = range(6)
        print("Enter 'q' to terminate connection")
        it = iter(seq)
        win = [next(it) for cnt in range(window_size)] # First window
        message = str(win[0])
        mySocket.send(message.encode())
        ack = mySocket.recv(1024).decode()                 
        print ('Server ACK: ' + ack)
        for e in it: # Subsequent windows
            win[:-1] = win[1:]
            win[-1] = e 
            message = str(win[0])
            mySocket.send(message.encode())
            ack = mySocket.recv(1024).decode()
            if ack ==0 :
                mySocket.send(message.encode())
                ack = mySocket.recv(1024).decode()
            print ('Server ACK: ' + ack)
        del win[0]
        for w in win:
            message = str(w)
            mySocket.send(message.encode())
            ack = mySocket.recv(1024).decode()
            if ack==0:
                print ('Server ACK: ' + ack)
                mySocket.send(message.encode())
                ack = mySocket.recv(1024).decode()
            print ('Server ACK: ' + ack)
        mySocket.close()
 
if __name__ == '__main__':
    Main()
