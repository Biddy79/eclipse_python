#!/usr/bin/python
# from _socket import *
# import optparse
# from threading import *
# 
# def main():
#     parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -P <taget port>')
#     parser.add_option('-H,', dest='tgtHost', type='string', help='specify target host')
#     parser.add_option('-P,', dest='tgtPort', type='string', help='specify target ports separated by comma')
#     (options, args) = parser.parse_args()
#     tgtHost = options.tgtHost
#     tgtPorts = str(options.tgtPort).split(',')
#     if (tgtHost == None) | (tgtPorts[0] == None):
#         print(parser.usage)
#         exit(0)
    #portScan(tgtHost,tgtPorts)
    
#main()

import argparse

def main():
    parser = argparse.ArgumentParser(description="Usage of program: -tgtHost <target host> -tgtPost <taget port>")

    #parser add argument   #name    #help description             #variable type
    parser.add_argument('-tgtHost', help = 'specify target host', type = str)
    parser.add_argument('-tgtPort', help = 'specify target ports separated by comma', type = str)
    
    #must set args = pareser argumets befor creating tgtHost and tgtPort = toarguments in parser
    args = parser.parse_args()
    
    #setting variables to argument
    tgtHost = args.tgtHost
    tgtPort = str(args.tgtPort).split(',')
    
    #checking if tgtHost or tgtPort are == to empty string if so print description
    if tgtHost == "" or tgtPort == "":
        print(parser.description)
        exit()
        
    #port scanner to be created!!!
    #portScan(tgtHost,tgtPorts)
        
    print(parser.description)
    
    
main()
    
