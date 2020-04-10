

# #list of items to be added to file 
# currencies = ["USD", "EURO", "GBP", "JPY"]
# 
# #writing to file using: with, as, and open(). Parameters for open when writing are: file path and 'w'
# with open("currencies.txt", 'w') as currency_file:
#     for currency in currencies:
#         #adding file=currency_file parameter will add currency items to the file
#         #print also as a flush parameter 
#         print(currency, file=currency_file)
#         
##################COMMENTED CODE ABOVE OUT AS FILE AS NOW BEEN CREATED################################

#reading currencies.txt file
with open("currencies.txt", 'r') as currency_file:
    for currency in currency_file:  
        #.strip(\n)removes the beginning or end characters from a string in this case the new line \n
        print(currency.strip('\n'))
        
print("-" * 30)

#creating a empty currencies list
currencies = []


with open("currencies.txt", 'r') as currency_file:
    for currency in currency_file:
        #appending all items from currency_file to currencies list
        currencies.append(currency.strip('\n'))
        
#currencies list printed out
print(currencies)

#print out using readline()
with open("currencies.txt",'r') as currency_file:
    line = currency_file.readline()
    while line:
        print(line, end='')
        line = currency_file.readline()
        
 

        
    