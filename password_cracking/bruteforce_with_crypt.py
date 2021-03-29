'''
Created on 28 Mar 2021

@author: Adam
'''
#!/usr/bin/python3

#crypt.crypt() function takes chars (password) and two capitalized letters as its salt


#crack_pass function arg crypt_word:
#crypt_word is the password that is hashed and salted 
#in out pass.txt file. We save the first two character (which is the salt)
#in a vareable called salt then after reading the passwords from our 
#dictionary.txt add the salt (two character) to the front of the password 
#and hash it using the crypt.crypt(word, salt) function.
#We then test for equality aginst the password in our pass.txt file (crypt_word)


#The main falut with this is that it assumes you would have the salted hash 
#to start with to strip the salt characters for it to perform your own hash
#and salt to search for a match


import crypt

def crack_pass(crypt_word):
    salt = crypt_word[0:2]
    with open('dictionary.txt', 'r') as dictionary:
        for word in dictionary.readlines():
            word = word.strip('\n')
            crypt_pass = crypt.crypt(word, salt)
            if (crypt_word == crypt_pass):
                print(f"password is : {word}")
                return
def main():
    with open('pass.txt', 'r') as pass_file:
        for line in pass_file.readlines():
            if ":" in line:
                user = line.split(':')[0]
                crypt_word = line.split(':')[1].strip(' ').strip('\n')
                print(f"[*] Checking {user} for password match")
                crack_pass(crypt_word)
        print("[-] Password not fount in dictionary")
            
    
main()