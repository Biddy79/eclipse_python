#!/usr/bin/python

import socket 
#termcolor must be download to os
from termcolor import colored



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(3)

host = int(input("[*] Enter host to scan: "))

port = int(input("[*] Enter port to scan: "))


def portScanner(port):
    if sock.connect_ex((host,port)):
        print(colored(f"port {port} closed", 'red'))
    else:
        print(colored.green(f"port {port} open", 'green'))

for port in range(1,2000):
    portScanner(port)
        



        
    
    
