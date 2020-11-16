#!/usr/bin/python3
#version 4

import socket
import os
import sys

#call to socket using ip and port. return banner 
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

#check file of vilnerable banners for match against returned banner
def checkVulns(banner, filename):
    #two list created
    fileList = []
    #splitting returned banner at new line into list
    bannerList = str(banner).split("\n")
    
    #adding banners to fileList, splitting at new line
    with open(filename, 'r') as bannerFile:
        for line in bannerFile:
            fileList += line.split("\n")
    
    #check to see if bannerList and fileList have any matching banners
    for b in bannerList:
        if b.replace("\\r\\n'", "") not in fileList:
            print(f"[+] No vulnerable banner found.")
    
    #check for macthing banners in bannerList and filelist and print 
    for x in fileList:
        for b in bannerList: 
            if x.strip("'") == b.replace("\\r\\n'", ""):
                print(f"[+] vulnerable banner found: {x}")        

#Ask user for .txt file (check file exists and can gain access)
#Print out usage of program if no file is given
#set ip and ports to scan
#call to checkVulns

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
        print(f"[-] Usage for : {sys.argv[0]} must add path file of <vulnerable banners.txt>")
        exit(0)

    portlist = [21,22,25,80,110,443,445]
    ip = "192.168.8.117"
    
    for port in portlist:
        banner = retBanner(ip,port)
        if banner:
            print("-" *  30)
            print(f"[+]Searching {ip}/{port} for vulnerable banners:")
            checkVulns(banner, filename)
            print("-" *  30)
    
main()            