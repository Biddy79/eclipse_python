'''
Created on 18 Oct 2021

@author: adam
'''
#!/usr/bin/pyhton3

import socket
import os, sys
import struct
import binascii

sock_created = False
sniffer_socket = 0

def analyze_ether_header(data_recv):
    ip_bool = False
    
    eth_hdr = struct.unpack('!6s6sH', data_recv[:14])
    dst_mac = binascii.hexlify(eth_hdr[0])
    src_mac = binascii.hexlify(eth_hdr[1])
    proto = eth_hdr[2] >> 8
    data = data_recv[14:]
    
    print("____________ETHERNET HEADER____________")
    print(f"Destination MAC: {dst_mac[0:2]}:{dst_mac[2:4]}:{dst_mac[4:6]}:{dst_mac[6:8]}:{dst_mac[8:10]}:{dst_mac[10:12]}")
    print(f"Source MAC: {src_mac[0:2]}:{src_mac[2:4]}:{src_mac[4:6]}:{src_mac[6:8]}:{src_mac[8:10]}:{src_mac[10:12]}")
    print(f"Protocol: {proto}")
    
    if proto == 0x08:
        ip_bool = True
        
    return data, ip_bool

def analyze_ip_header(data_recv):
    ip_hrd = struct.unpack('!6H4s4s', data_recv[:20])
    

def main():
    if sock_created == False:
        sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0X0003))
        sock_created = True
        
    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    
    data_recv, ip_bool = analyze_ether_header(data_recv)
    
    if ip_bool:
        data_recv, tcp_udp = analyze_ip_header(data_recv)
    else:
        return
    
    
    
    
    
    
    
    
    
    