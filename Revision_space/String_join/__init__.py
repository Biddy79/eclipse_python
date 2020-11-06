#Python string method join() returns a string in which the 
#string elements of sequence have been joined by str separator.

seq = "abc"

new_seq = ' '.join(seq)

print(new_seq)


my_list = "I like winter"
#' '.join(my_list) this will add a blank space between each leatter 
# including its own white spaces
my_list2 = ' '.join(my_list)
# 0 1 2 3 4 5 6 7 8 9 . . . . . . . . . . . . . .
#[I, , , ,l, ,i, ,k, ,e, , , ,w, ,i, ,t, ,e, ,r, ]
print(my_list2)

#so this would make element 14 in my_list2 the letter w
print(my_list2[14])

#split performs the oppersite way and removes the element give in its parameter 
#NO PARAMITER  = ' ' SPACE

my_list3 = my_list2.split()

print(my_list3)
# 0 1 2 3 4 5 6 7 8 9 
#[I,l,i,k,e,w,i,t,e,r]

#so this would now make element 5 in my_list3 the letter w
print(my_list3[5])