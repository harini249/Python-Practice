# [Non local variable]

# variable can be defined within the outer function and above inner function  is non local function

def parent(): # outer function
    items = ["Rice","Milk"]
    print("In Outer function :",items)

    
    def child():  # inner function 
        print("In inner function : ",items)
        
    child()

parent()


