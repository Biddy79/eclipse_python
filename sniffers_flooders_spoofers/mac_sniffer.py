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
    
    #selecting first 14 bytes from first packets[0]
    #the first 14 bytes holds the ether info 
    eth_lenght = 14
    eth_header = packet[:eth_lenght] 
    
    #unpack from struct takes binary data and corectly formats it from C structs
    
    #First parameter ! is the format type (network=big-endian) of data
    #there are many other formats that can be use !, @, =, <, and >
    
    #6 is the number of bytes from the eth_header
    #s identifies these 6 bytes as a char[] (string). the first 6 bytes are the 
    #destination mac address. 
    
    #We then do the same to get the next 6 bytes
    #which is the source mac address.
    
    #Finaly we have the H parameter which is the ether protocol. The type is an
    #unsigned short. (an unsigned short is 2 bytes) 
    #this all together makes 14 bytes
    eth = unpack('!6s6sH', eth_header)
    
    #Saving the 3rd eliment from eth object above. eth[2] which is H. This is 
    #the ether protocol which is a number representing tcp, udp, http ect ...
    #agine we use socket.ntohs to convert to host format 
    eth_protocol = socket.ntohs(eth[2])
    
    
    
    
