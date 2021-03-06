#!/usr/bin/python3
#version 1

import socket
import os
import sys


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
    f = open(filename, "r")
    for line in f.readline():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable:" + banner.strip("\n"))



def main():
 
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
            