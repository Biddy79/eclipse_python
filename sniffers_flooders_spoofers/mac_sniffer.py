'''
Created on 6 Jun 2021

@author: adam
'''

#!/usr/bin/python3

import socket
from struct import *


try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
    print("[!!] Error on creating socket object")
    exit(0)
    