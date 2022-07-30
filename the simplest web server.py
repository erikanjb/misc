from socket import *

def createserver():
    #make a socket...make a phone ...and endpoint
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        #waiting on port 9000 to recieve the phonecalls
        serversocket.bind(("localhost",9000))
        #the 5 says if on 1 phone call qeue the remaining 4
        serversocket.listen(5)
        while(1):
            #accept means ..ready to picup the phone..
            (clientsocket, address) = serversocket.accept()
            
            #this line runs only when a phonecall is recieved
            #decode
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            #print the url to show that you recieved
            if ( len(pieces) > 0 ) : print(pieces[0])
            #construct a response
            data = "HTTP/1.1 200 OK\r\n"
            data += "content-TYPE: text/html; charset=uf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\n"
            #encode to ucf8
            clientsocket.sendall(data.encode())
            #close the connection
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
         print("\nshutting down...\n");
    except Exception as exc :
         print ("Error:\n");
         print (exc)

    serversocket.close()
print("access http://localhost:9000")
createserver()
     
