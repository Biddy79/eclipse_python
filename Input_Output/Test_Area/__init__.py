import shelve

with shelve.open('some_data') as some_data:
    print(some_data["data_0"])