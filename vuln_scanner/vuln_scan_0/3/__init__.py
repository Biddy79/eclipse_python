#!/usr/bin/python3
#version 3

import socket
import os
import sys
from pip._vendor.pyparsing import line


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, filename):
    fileList = []
    #spliting returned banner at new line into list
    bannerList = str(banner).split("\n")
    
    #adding banners (spliting at new elements at new line) to fileList
    with open(filename, 'r') as bannerFile:
        for line in bannerFile:
            fileList += line.split("\n")
    
    #printing elements in fileList
    for f in fileList:
        print(f.strip("'"))
    
    print("----------------------")
    #printing elements in bannerList
    #replace("\\r\\n", "") this replaces \\r and \\n with empty string
    for b in bannerList:
        print(b.replace("\\r\\n\'", ""))
            
    print("----------------------")
    
    #cheking to see if banner in bannerList is in fileList
    for x in fileList:
        for b in bannerList:
            if x.strip("'") == b.replace("\r\n\'", ""):
                print("banner match")
            elif x != b:
                print("No banner match")
        
def main():
    filename = ""
 
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File dose not exist!")
        if not os.access(filename, os.R_OK):
            print("[-] File Access Denied!")
            exit(0)
    else:
        print(f"[-] Usage for : {sys.argv[0]} must add path file of <vuln.txt>")
        exit(0)

    portlist = [21,22,25,80,110,443,445]
    ip = "192.168.8.117"
        
    for port in portlist:
        banner = retBanner(ip,port)
        if banner:
            print(f"[+] {ip}/{port} : banner")
            checkVulns(banner, filename)
            

main()            