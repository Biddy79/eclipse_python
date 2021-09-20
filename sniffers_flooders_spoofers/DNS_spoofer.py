'''
Created on 27 Aug 2021

@author: adam
'''
#!/usr/bin/python   

#May not work in python 3 may need to use python 2
#!/usr/bin/env python2.7

from scapy.all import * 
from netfilterqueue import NetfilterQueue

def proces_packet(packet):
    pkt = IP(packet.get_payload()) #converts the raw packet to a scapy compatible string

    #modify the packet here

    packet.set_payload(str(pkt)) #set the packet content to our modified version

    packet.accept() #accept the packet
    
    

nfqueue = NetfilterQueue()
#0 is the iptabels rule queue number, modify is the callback function
nfqueue.bind(0, proces_packet) 

try:
    print "[*] waiting for data"
    nfqueue.run()
except KeyboardInterrupt:
    
    