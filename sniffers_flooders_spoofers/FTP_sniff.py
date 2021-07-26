'''
Created on 23 Jul 2021

@author: adam
'''

#!/usr/bin/pyhton3

from scapy.all import *
import argparse

def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    

def mian():
    #Instantiate argparse variable
    parser = argparse.ArgumentParser(descrtiption='Usage of program: -i <interface>')
    
    #add argument to parser obj. parameters: name, help description, variable type
    parser.add_argument('-i', help='Interface', type=str)
    
    #arg variable of parse_args(). 
    #(args is used to set our own veriables to)
    args = parser.parse_arg()
    
    #Variable interface set equal to -i within the parser
    interface = args.i
    
    #set interface equal to user iuput
    if interface == None:
        print(parser.descrtiption)
        exit(0)
    else:
        conf.iface = interface
    #Start sniff, fillter to sniff only tcp port. 
    #prn process packets passed to ftpSniff function
    try:
        sniff(filter='tcp port 21', prn=ftpSniff)
    except:
        KeyboardInterrupt:
        exit(0)
    
    
    
    