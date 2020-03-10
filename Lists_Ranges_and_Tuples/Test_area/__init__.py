sing_in_record = ("B.A", 21, [00.00, 00.00])

#initials, age, time = sing_in_record 
# print(initials)
# print(age)
# print(time[0], time[1])

user_input = input(print("Enter first and last initials, your age time in and out"))

user_input = "".join(user_input.split())

# print(user_input[0:2])
# print(user_input[2:4])
# print(user_input[4:9])
# print(user_input[9:14])



for info in user_input:
    for time in info:
        info[0:2], info[2:4], time[4:9], time[9:14] = sing_in_record




    
