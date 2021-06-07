'''
Created on 6 Jun 2021

@author: adam
'''

#!/usr/bin/python3

import socket
from struct import *

#ntohs() function of socket module converts a 16 bit integer
#from network format to host format. 
#parameter 0x0003 in hexadecimal for the number 3 and there we are using 
#GGP protocol. you can also do the same using getprotoent(GGP)

try:                                                     
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
    print("[!!] Error on creating socket object")
    exit(0)

#The recvfrom() method Python's socket class, reads a number of bytes sent from an UDP socket.

#The return value is a pair (string, address) where string is a string representing
#the data (remember data is in bytes!) received and address is the address of the socket sending the data.

#s.recvfrom() parameter 65535 is port number.
#This will first recive packet from port 1 then 2 and so on ...
#untill it reaches port 65535 as is inside the while Ture loop.

while True:
#setting the packet to recive the first part of the tuple
#a string in bytes format. The second part, packet[1]
#would be the address as stated on line 25 above
    packet = s.recvfrom(65535)
    packet = packet[0] 
    
#setting eth_lenght to be 14.
#used below to set number of bytes we require 
#from (bytes)string info given in packet[0] above 
    eth_length = 14
     
#selecting first 14 bytes from first packet[0]
#the first 14 bytes holds the eth info 
    eth_header = packet[:eth_length] 
    

    
    # may be usfull       print(receivedBytes[0].decode());!!!!!!!!