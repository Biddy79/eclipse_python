#!usr/bin/python

import socket 
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(3)

host = raw_input("[*] Enter host to scan: ")

#port = int(input("[*] Enter port to scan: "))


def portScanner(port):
        if sock.connect_ex((host,port)):
            print(colored("port %d closed" % (port), 'red'))
        else: 
            print(colored("port %d open"  %(port), 'green'))

for port in range(1,2000):
    portScanner(port)
        



        
    
    