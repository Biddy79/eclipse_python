import socket
from typing import cast

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(3)

host = input("[*] Enter the host to scan: ")

port = int(input("[*] Enter the port to scan: "))

def portScanner(port):
    if sock.connect_ex((host,port)):
        print("port %d is closed" %(port)) 
    else:
        print("port %d is open" %(port)) 
        
portScanner(port)

