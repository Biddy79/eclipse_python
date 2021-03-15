'''
Created on 15 Mar 2021

@author: Adam
'''

#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored


#Ask user to input password sha1 value
sha1hash = input("[*] Enter a sha1 Hash value: ")

#store list of passwords form website github
password_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt').read(), 'utf-8')   

#read passwords in password_list
for password in password_list.split('\n'):
    #store value of password after coverting to sah1 and casting to bytes
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    #check for match 
    if hashguess == sha1hash:
        #print out password after casting back to string
        print(colored(f"[*] The password is: {str(password)}", 'green' ))
        quit()
    else:
        print(colored(f"[-] password guess {str(password)} dose not match trying next password ...", 'red'))
        
#After tying all pawsord in list if none is found this message will print
print("Pssword not found in password list")
        
