#!usr/bin/python

import socket 


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(3)

host = input("[*] Enter host to scan: ")
port = int(input("[*] Enter port to scan: "))


def portScanner(port):
    if sock.connect_ex((host,port)):
        print("port %d closed") %(port)
    else: 
        print("port %d open")  %(port)
        
portScanner(port)
        



        
    
    