#!/urs/python3

import pexpect

def connect(user, host, password):
    

def send_command():
    

def main():
    host = input("Enter host ip:")
    user = input("Enter user:")
    password = input("Enter password:")
    
    #child is set = to connect function 
    child = connect(user,host,password)
    
    #call to send_comand function 
    send_command(child, 'cat /ect/shadow | grep root;ps')
    
main()