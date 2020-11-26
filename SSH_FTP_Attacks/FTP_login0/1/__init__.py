#Runs a FTP login attack on given host using anonymous as username and password. 
#Some servers will allow admin to log in with anonymous as credentials.


#!/usr/bin/python3

import ftplib

def annonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print(f"[+] {hostname} login successful")
        return True
    except:
        print(f"[-] {hostname} login failed")
        

host = input("Enter Ip Address:")
annonLogin(host) 