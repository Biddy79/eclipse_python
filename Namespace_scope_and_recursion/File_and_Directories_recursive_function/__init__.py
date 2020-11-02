import os 


def list_directories(s):
    
    def dir_list(d):
        nonlocal tab_stop # nonlocal looks for veriabel within the encloseing scope. not defined!!
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)
    
    
    tab_stop = 0 # tab_stop veriabel is within the encloseing scope of list_directories function 
    if os.path.exists(s):
        print('directory listing of ' + s)
        dir_list(s)
    else:
        print(s+ " Does not exist")
    

list_directories('.')
