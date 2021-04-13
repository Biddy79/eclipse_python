'''
Created on 13 Apr 2021

@author: Adam
'''
#!/usr/bin/python3


from scapy.layers.l2 import ARP, Ether
from scapy.all import *



def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = srp(finalpacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)
    
#def spoof_arp(target_ip, spoofed_ip):
    

def main():
    target_ip = input("[*] Enter target ip: ")
    get_mac(target_ip)
#     spoofed_ip = input("[*] Enter spoofed ip: ")
#     try:
#         while True:
#             spoof_arp(spoofed_ip, target_ip)
#             spoof_arp(target_ip, spoofed_ip)
#             
#     except KeyboardInterrupt:
#         exit(0)

main()