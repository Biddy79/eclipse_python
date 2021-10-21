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
    
    #set packet data byte to start from remaning 14 bytes
    data = data_recv[14:]
    
    print("____________ETHERNET HEADER____________")
    print(f"Destination MAC: {dst_mac[0:2]}:{dst_mac[2:4]}:{dst_mac[4:6]}:{dst_mac[6:8]}:{dst_mac[8:10]}:{dst_mac[10:12]}")
    print(f"Source MAC: {src_mac[0:2]}:{src_mac[2:4]}:{src_mac[4:6]}:{src_mac[6:8]}:{src_mac[8:10]}:{src_mac[10:12]}")
    print(f"Protocol: {proto}")
    
    #check packet to see if it is ip protocal
    if proto == 0x08:
        ip_bool = True
    
    #return packet bytes starting at 14 and protocoal type
    return data, ip_bool


# >> (Right-Shift) and << (Left-Shift) Operator: Moves the bits the number
# of positions specified by the second operand in the right or left direction
# 0x0F is a hexadecimal number which equals 15 in decimal
def analyze_ip_header(data_recv):
    ip_hdr = struct.unpack('!6H4s4s', data_recv[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0]) >> 8 & 0x0f
    tos = ip_hdr[0] & 0x00ff
    tot_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flags = ip_hdr[3] >> 13
    frag_offset = ip_hdr[3] & 0x1fff
    ip_ttl = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    checksum = ip_hdr[5]
    src_address = socket.inet_ntoa(ip_hdr[6])
    dst_address = socket.inet_ntoa(ip_hdr[7])
    
    print("______________IP HEADER_______________")
    print(f"Version: {ver}")
    print(f"IHL: {ihl}")
    print(f"TOS: {tos}")
    print(f"Lenght: {tot_len}")
    print(f"ID: {ip_id}")
    print(f"Flags: {flags}")
    print(f"Offset: {frag_offset}")
    print(f"TTL: {ip_ttl}")
    print(f"Proto: {ip_proto}")
    print(f"Checksum: {checksum}")
    print(f"Source IP: {src_address}")
    print(f"Destination IP: {dst_address}")
    
    #set packet data byte to start from remaning 20 bytes
    data = data_recv[20:]
    
    #check protocal type
    if ip_proto == 6:
        tcp_udp = "TCP"
    elif ip_proto == 17:
        tcp_udp = "UDP"
    else:
        tcp_udp = "OTHER"
    
    #return packet bytes starting at 20 and protocoal type
    return data, tcp_udp
    
    
def main():
    if sock_created == False:
        sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0X0003))
        sock_created = True
        
    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    
    #data returned from analyze_ether_header sets data_recv to start at 14 bytes
    data_recv, ip_bool = analyze_ether_header(data_recv)
    
    #data returned from analyze_ip_header sets data_recv to start from 20 bytes
    if ip_bool:
        data_recv, tcp_udp = analyze_ip_header(data_recv)
    else:
        return
    
    
    
    
    
    
    
    
    
    