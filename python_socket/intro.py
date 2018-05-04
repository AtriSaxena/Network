import socket
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print(s)
server = 'www.google.com'
port = 80
server_ip= socket.gethostbyname(server)
print(server_ip)
request = "GET/ HTTP/1.1\n Host:" + server+"\n\n"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.nitj.ac.in",22))
s.send(request.encode())
result = s.recv(4096)   #4096 is the buffer of the data we receive in chunks
print(result)
