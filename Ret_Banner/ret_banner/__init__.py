#!/usr/bin/python

import socket

def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket()
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner
    except:
        return

def main():
    ip = input("[+] Enter ip: ")
    for port in range(0, 1000):
        banner =  ret_banner(ip, port)
        if banner:
            print("[+]" + ip + ": " +  banner.strip('\n'))
            
main()
