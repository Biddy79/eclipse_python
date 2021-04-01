'''
Created on 1 Apr 2021

@author: Adam
'''
#!/usr/bin/python3

import subprocess
from termcolor import colored


def change_mac(interface, mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", mac])
    subprocess.run(["ifconfig", interface, "up"])

def main():
    interface = input("[*] Enter Interface of mac address you would like to change: ")
    input_mac_add = input("[*] Enter a new mac address: ")
    
    current_mac_add = subprocess.check_output(["ifconfig", interface])
    change_mac(interface, input_mac_add)
    new_mac_add = subprocess.check_output(["ifconfig", interface])
    
    if current_mac_add == new_mac_add:
        print(colored(f"[!!] Failed to change mac address to {input_mac_add}", 'red'))
    else:
        print(colored(f"[+] mac address sucsesfully changed to {input_mac_add}", 'green'))

    
main()