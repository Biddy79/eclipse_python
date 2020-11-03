#nested function have acsess to veriabels in the inner scope the outer scope dose not 
#y veriabel in spam2 function can be called with in spam3 
#likewise x veriabel declared in spam 1 can be called within spam2 function

# locals() function added to show local veriabels 
def spam1():
    
    def spam2():
        
        def spam3():
            #here we are inside spam3
            z = " even"
            z += y
            print(f"In spam3, locals are {locals()}")
            return z
        #here we are inside spam2
        y = " more " + x
        y += spam3()
        print(f"In spam2, locals are {locals()}")
        return y
    #here we are inside spam1
    x = "spam,"
    x += spam2()
    print(f"In spam1, locals are {locals()}")   
    return x

print(spam1())