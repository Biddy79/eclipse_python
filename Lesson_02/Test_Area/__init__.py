num = 13

for i in range(num):
    print(i * 5)


name = "Jimbo jones the man with no bones"

for char in name:
    print(char, end = '')
    
print()

user_description = ["1: name", "2: age", "3: gender", "4: hight"]

user_input = ""


while True:
    user_input = input("SELECT OPTION 1,2,3, or 4: ")
    if user_input == "0":
        print("good buy")
        break
    elif user_input in "1234":
        print(f"You selected {user_input}")
    elif user_input not in "1234":
        print(f"You made an invalid selection.....")
    
    
    
    

        
    
        
        


   
    
    
    
    
    

