colours = "Red Green Blue"

for character in colours:
    print(character)
    
print("-" * 20)
    
number = "992, 47: 36;38 875;1123"
separators = ""

for char in number:
    if not char.isnumeric(): # isnumeric() checks for numbers in string
        separators = separators + char
        
print(separators)
