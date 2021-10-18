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
    


def main():
    if sock_created == False:
        sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0X0003))
        sock_created = True
        
    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    
    formated_data_recv, ip_bool = analyze_ether_header(data_recv)