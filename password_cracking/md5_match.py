'''
Created on 16 Mar 2021

@author: Adam
'''
#!/usr/bin/python3

import hashlib
from termcolor import colored

#input md5 hash to find match
md5_hash = input("[*] Enter a md5 hash value: ")
#input file path containing list of password
word_list = input("[*] Enter file path containing password list: ")

#try to open file. If file not found print out to user
def try_open(word_list):
    global pass_file
    try:
        pass_file = open(word_list, 'r')
    except:
        print("[!!] File path not found!")
        quit()

try_open(word_list)
        
#search through word in file after coverting to md5 hash to find match
for word in pass_file:
    print(colored("[-] Trying: " + word.strip('\n'), 'red'))
    
    #Converts the string into bytes to be acceptable by hash function
    encode_wrd = word.encode('utf-8')
    
    #hashlib.md5() takes encoded string and convert into md5 hash 
    #hexdigest() Returns the encoded data in hexadecimal format.
    md5_digest = hashlib.md5(encode_wrd.strip()).hexdigest()
    
    #check md5 hash passed in by user on line11 for match against 
    #md5 hashed word in file
    if md5_digest == md5_hash:
        print(colored(f"[+] Password match found {word} ", 'green'))
        exit(0)
        
#If no password is matched display to user 
print("[!!] No password match found in list! ")



    