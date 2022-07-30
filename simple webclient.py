import socket

#make a phone...

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to localhost...ipv4 connection....port 9000 is where our web server is running 
mysock.connect(("127.0.0.1",9000))
#send a get request...and encode it into utf8
cmd = "GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n".encode()
#send
mysock.send(cmd)
#loop that prints it all out

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end=" ")
    
#close the socket...hang up the phone 
mysock.close()
    
