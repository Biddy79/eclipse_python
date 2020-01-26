import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.8.104"

port = 443

def portScanner(port):
    if sock.connect_ex((host, port)):
        print("Port %d is closed" %(port)) 
    else: 
        print("Port %d is open" %(port))
        
portScanner(port)
        


