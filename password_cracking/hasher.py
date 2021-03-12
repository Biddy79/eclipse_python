'''
Created on 12 Mar 2021

@author: Adam

hash user input to md5, sha1, sah224, sha256 and sha512

'''

import hashlib
#ask user to pass in a password to hash
hash_value = input("* Enter a password to hash: ")


#set hashObj1 equal to md5 type hash
hashObj1 = hashlib.md5()
#pass hash_value given by user to hashObj1 to be encoded as md5 hash
hashObj1.update(hash_value.encode())
#print md5 hash to console
print(hashObj1.hexdigest())


#sha1 hash /////same as above but encodeing function called inside of hashlib/////
hashObj2 = hashlib.sha1(hash_value.encode())
print(hashObj2.hexdigest())


#sha224
hashObj3 = hashlib.sha224(hash_value.encode())
print(hashObj3.hexdigest())


#sha256
hashObj4 = hashlib.sha256(hash_value.encode())
print(hashObj4.hexdigest())


#sha512
hashObj5 = hashlib.sha512(hash_value.encode())
print(hashObj5.hexdigest())

