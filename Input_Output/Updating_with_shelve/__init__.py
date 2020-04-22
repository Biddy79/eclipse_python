import shelve

#lists of items created
list_0 = ["tooth paste", "bread" , "milk"]
list_1 = ["cake", "beans", "toilet roll"]

#we can add new list here and run code again to add list to shopping_lists file
list_3 = ["butter", "soup"]

#lists_0 and list_1 added to shopping_list file as shopping_list 
with shelve.open('shopping_lists') as shopping_lists:
    shopping_lists['my_list'] = list_0
    shopping_lists['mums_list'] = list_1
    #then added list_3 here to update with list_3
    shopping_lists['Brothers_list'] = list_3
    
    items = shopping_lists['my_list'] + shopping_lists['mums_list']
    
    print(f"Items required form shop {items}")
    #I can now print out brothers_list as it been added to shopping_list file
    print(f"Brother wants {shopping_lists['Brothers_list']}")
    
    print("-" * 30)

#You can not update individual items of a list in shelve using append() function eg:
    shopping_lists['my_list'].append("BACON")
#as we can see BACON was NOT added to my_list
    for lists in shopping_lists:
        print(lists, shopping_lists[lists])
        
    print("-" * 30)
    
#One way you CAN append to a list stored in a shelve is to create a temp_list to store items 
    temp_list = shopping_lists['my_list']
    temp_list.append("BACON")
    shopping_lists['my_list'] = temp_list
#now we can see BACON was added to my_list
    for lists in shopping_lists:
        print(lists, shopping_lists[lists])

#####################################################################################      
#another way to update items to a list in shelve is to use parameter writeback=True 
#shelve.open('shopping_lists, writeback=True)

#we could then use append() function with shelve
    #shopping_lists['my_list'].append("BACON")

#down side to writeback=True. Heavy memory usage when working with large file and could take a long time
#to update when closing file to update 
####################################################################################        
        
####################################################################################
#one more way to update items to a list in shelve is to use sync function TAKE CARE to use sync()
#after making changes or shelve will not be updated
#shopping_list['my_list].append("BACON")
#shopping_lists.sync()

        
        
        
        
    

        
    


