'''
Created on 27 Aug 2021

@author: adam
'''
#!/usr/bin/python3

from scapy.all import * 

def find_DNS(p):
    if p.haslayer(DNS):
        print(p[IP].src, p[DNS].summary())

sniff(prn=find_DNS)