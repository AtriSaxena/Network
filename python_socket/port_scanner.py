import socket


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

##target = input('What website you want to scan?:')

target='https://www.hackthissite.org/'
def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False

for x in range(60,90):
        print('Port',x,'is open')
    if pscan(x):
    else:
        print('Port',x,'is close')
