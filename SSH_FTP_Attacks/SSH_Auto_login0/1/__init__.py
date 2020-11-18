#!/urs/python3

#Remote log in ssh login.
 
#Automating ssh log in using pexpect. Pexpect will give a command or call to run automatically.

#first it will give command using pexpext.spawn() and call parameters passed in.
 
#After sotering in a variable (child) we can then use function call expect() which
#gives expected return values form the call made or sendline() function which will send a string
#this can be inturpreted as the next given command.

import pexpect

#list of input prompts that may be givne in terminal after login in to ssh
PROMPT = ['# ', '>>> ', '> ', '\$ ']

#sending commands to run on target system and any given expeected prompts. receving response
def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    #child.befor will print output form target system 
    print(child.before)
    
    
    
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
    child.expect(PROMPT)
    return child
    


    

def main():
    host = input("Enter host ip:")
    user = input("Enter user:")
    password = input("Enter password:")
    
    #child is set = to connect function 
    child = connect(user,host,password)
    
    #call to send_comand function 
    send_command(child, 'cat /ect/shadow | grep root;ps')
    
    
main()