# [Non local variable]

# variable can be defined within the outer function and above inner function  is non local function

def shopping(): # outer function
    item1 ,item2 = "Rice","Milk"
    print("In Outer function :",item1, item2)

    
    def show_items():  # inner function 
        print("In inner function : ",item1,item2)
        
    show_items()

shopping()


