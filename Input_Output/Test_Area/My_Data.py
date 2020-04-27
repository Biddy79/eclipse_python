'''
Created on 27 Apr 2020
 
@author: Adam
'''
import shelve
 
some_data = shelve.open('some_data')
 
#note last dict element is of list type
some_data["data_0"] = {"1": "abc",
                       "2": "efg",
                       "3": "hij",
                       "4": ['k','l','m']}
 
some_data.close()