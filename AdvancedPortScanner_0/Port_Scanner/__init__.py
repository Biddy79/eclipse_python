#!/usr/bin/python3

import argparse
from _socket import * 
from threading import * 

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(f"[+] {tgtPort}/tcp Open")
    except:
        print(f"[-] {tgtHost}/tcp Closed")
    finally:
        sock.close()
        
    

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"Unknown Host {tgtHost} ")
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan results for:" + tgtName[0])
    except:
        print("[+] Scan results for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args=(tgtHost, int(tgtPort)))
        t.start()
    
    
def main():
    parser = argparse.ArgumentParser(description="Usage of program: -H <target host> -p <taget port>")

    #parser add argument #name    #help description             #variable type
    parser.add_argument('-H', help = 'specify target host', type = str)
    parser.add_argument('-p', help = 'specify target ports separated by comma', type = str)
    
    #must set args = pareser argumets befor creating tgtHost and tgtPort = toarguments in parser
    args = parser.parse_args()
    
    #setting variables to argument
    tgtHost = args.H
    tgtPorts = str(args.p).split(',')
    
    #checking if tgtHost or tgtPort are == to empty string if so print description
    if tgtHost == None or tgtPorts[0] == None:
        print(parser.description)
        exit(0)
    else:
        print(f"Host Entered: {tgtHost}  Port Entered: {tgtPorts}")
        
    #portScan function called
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()
    
    

    
