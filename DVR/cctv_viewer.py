'''
Created on 15 Mar 2021

@author: Adam
'''

#http://192.168.68.60/m.html?ch=0
#http://admin:1105@192.168.68.60:80
#https://192.168.68.60:80/user=admin/password=1105


import cv2
from urllib.request import urlopen


def ccvt():
    stream = urlopen("https://192.168.68.60:80/user=admin/password=1105/m.html?ch=0")

    capture = cv2.VideoCapture(stream)


    frames = capture.read()
    cv2.imshow(frames)


if __name__ == '__main__':
    print("ccvt")
    ccvt()
