'''
Created on 18 Oct 2021

@author: adam
'''
#!/usr/bin/python3

import socket
import os, sys
import struct
import binascii


def analyze_ether_header(data_recv):
    ip_bool = False
    
    eth_hdr = struct.unpack('!6s6sH', data_recv[:14])
    dst_mac = binascii.hexlify(eth_hdr[0])
    src_mac = binascii.hexlify(eth_hdr[1])
    proto = eth_hdr[2] >> 8
    
    print("____________ETHERNET HEADER____________")
    print(f"Destination MAC: {dst_mac[0:2]}:{dst_mac[2:4]}:{dst_mac[4:6]}:{dst_mac[6:8]}:{dst_mac[8:10]}:{dst_mac[10:12]}")
    print(f"Source MAC: {src_mac[0:2]}:{src_mac[2:4]}:{src_mac[4:6]}:{src_mac[6:8]}:{src_mac[8:10]}:{src_mac[10:12]}")
    print(f"Protocol: {proto}")
    
    #check proto (on line 22) to see if it is ip protocal
    if proto == 0x08:
        ip_bool = True
        
    #MOVE PACKET DATA 14 FORWARD BYTES!!
    data = data_recv[14:]
    
    #return packet data (this as now been moved on 14 bytes. see line: 34) and protocoal type
    return data, ip_bool


# >> (Right-Shift) and << (Left-Shift) Operator: Moves the bits the number
# positions specified by the second operand in the right or left direction
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
    
    #check protocal type
    if ip_proto == 6:
        tcp_udp = "TCP"
    elif ip_proto == 17:
        tcp_udp = "UDP"
    else:
        tcp_udp = "OTHER"
        
    #MOVE PACKET DATA 20 FORWARD BYTES!!
    data = data_recv[20:]
    
    #return packet data (this as now been moved on 20 bytes. see line: 81) and protocoal type
    return data, tcp_udp
    
    
def analyze_tcp_header(data_recv):
    tcp_hdr = struct.unpack('!2H2I4H', data_recv[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    seq_num = tcp_hdr[2]
    ack_num = tcp_hdr[3]
    data_offset = tcp_hdr[4] >> 12
    reserved = (tcp_hdr[5] >> 6) & 0x03ff
    flags = tcp_hdr[4] & 0x003f
    window = tcp_hdr[5]
    checksum = tcp_hdr[6]
    urg_ptr = tcp_hdr[7]
        
    #using flags variable above to split each flag represented by it bytes
    urg = bool(flags & 0x0020)
    ack = bool(flags & 0x0010)
    psh = bool(flags & 0x0008)
    rst = bool(flags & 0x0004)
    syn = bool(flags & 0x0002)
    fin = bool(flags & 0x0001)
    
    
    print("______________TCP HEADER_______________")
    print(f"Source: {src_port}")
    print(f"Destination: {dst_port}")
    print(f"Source: {src_port}")
    print(f"Seq: {seq_num}")
    print(f"ACK: {ack_num}")
    print(f"Data Offset: {data_offset}")
    
    print("___FLAGS___ ")
    print(f"flag-URG: {urg}")
    print(f"flag-ACK: {ack}")
    print(f"flag-PSH: {psh}")
    print(f"flag-RST: {rst}")
    print(f"flag-SYN: {syn}")
    print(f"flag-FIN: {fin}")
    
    print(f"Window size: {window}")
    print(f"Checksum: {checksum}")
        
    #MOVE PACKET DATA 20 FORWARD BYTES!!
    data = data_recv[20:]
    
    #return packet data (this as now been moved on 20 bytes. see line: 128) 
    return data
    
def analyze_udp_header(data_recv):
    udp_hdr = struct.unpack('!4H', data_recv[:8])
    src_port = udp_hdr[0]
    dst_port = udp_hdr[1]
    lenght = udp_hdr[2]
    checksum = udp_hdr[3]
    
    print("______________UDP HEADER_______________")
    print(f"Source: {src_port}")
    print(f"Destination: {dst_port}")
    print(f"Lenght {lenght}")
    print(f"Checksum {checksum}")
    
    ##MOVE PACKET DATA 8 FORWARD BYTES!!
    data = data_recv[8:]
    
    #return packet data (this as now been moved on 20 bytes. see line: 147) 
    return data
    
        
    
def main():
    sock_created = False
    sniffer_socket = 0
    
    if sock_created == False:
        sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0X0003))
        sock_created = True
        
    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    
    #data returned from analyze_ether_header as moved forward 14 bytes and stored in data_recv 
    data_recv, ip_bool = analyze_ether_header(data_recv)
    
    #if ip header is true 
    #data returned from analyze_ip_header moved forward 20 bytes and stored in data_recv
    #Set value of tcp_udp to "TCP" or "UDP
    if ip_bool:
        data_recv, tcp_udp = analyze_ip_header(data_recv)
    else:
        return
    
    #run analyze_tcp_header or analyze_udp_header function based on tcp_udp 
    #return value set in analyze_ip_header
    #Agine data_recv will be moved forward 20 bytes
    if tcp_udp == "TCP":
        data_recv = analyze_tcp_header(data_recv)
    elif tcp_udp == "UDP":
        data_recv = analyze_udp_header(data_recv)
    else:
        return
        
    
while True:
    main()
    
    
    
    
    
    
    
    
    