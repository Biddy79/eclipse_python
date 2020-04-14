#writing to bin file using mode 'bw'

#we are using write() function to write to bin file. NOte we have to pass [i] as list and cast to bytes([i])
#the bytes([i]) function returns an immutable array
with open("simple.bin", 'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

#A better way to write the above would be to remove to for loop. Therefore we no longer need to pass 
#a list, ([i]) 
with open("simple.bin", 'bw') as bin_file:
    bin_file.write(bytes(range(17)))
        
#reading from bin file using mode 'br'

#This will read simple.bin file 
with open("simple.bin", 'br') as binFile:
    for b in binFile:
        print(b)
           
             #Numbers in hex
a = 65534    #FF FE
b = 65535    #FF FF       #note numbers after 65535 need 4 bytes to represent them
c = 65536    #00 01 00 00
x = 2998302  #02 2D C0 1E

#Take note of the 'big' and 'littel' parameter in to_byte() function. this is for byte ordering

#In computing, endianness refers to the order of bytes (or sometimes bits)
#within a binary representation of a number.
#It can also be used more generally to refer to the internal ordering of any representation,
#such as the digits in a numeral system or the sections of a date. 

#bin_file(2, big) parameters number of bytes and endianness
with open("binary_endianness.bin", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big',))
    bin_file.write(b.to_bytes(2, 'big',))
    bin_file.write(c.to_bytes(4, 'big',))
    #here we write x in both 'big' and 'littel' endianness
    bin_file.write(x.to_bytes(4, 'big',))
    bin_file.write(x.to_bytes(4, 'little',))

    
#reading binary_endianness.bin

with open("binary_endianness.bin", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')  
    print(e)                                    
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)
    
    
    

    