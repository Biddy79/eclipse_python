'''
Created on 25 Mar 2021

@author: Adam
'''
import bcrypt

#b befor a sting will cast to byte type object
word = b"admin"

#hashpw args: string converted to byte : gensalt random salt
#gensalt also takes an int. higher number gives better encryption but takes more resource
crypt_word = bcrypt.hashpw(word, bcrypt.gensalt())
 
print(crypt_word)

#checkpw check match args: string converted to byte : hashed and salted password
if bcrypt.checkpw(word, crypt_word):
    print("password match")
else:
    print("password dose not macth")
    
print("=" * 30)

#we can also cast str to a bytes object using .encode("utf-8")
word1 = "admin123".encode("utf-8")

print(type(word1))
crypt_word1 = bcrypt.hashpw(word1, bcrypt.gensalt())
print(crypt_word1)