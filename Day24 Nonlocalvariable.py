# Non loca variable

# variable can be defined within the outer function and above inner function  is non local function

def shopping():
    item1 ,item2 = "Rice","Milk"
    print(item1, item2)
    def show_items():
        print(item1,item2)
        
    show_items()

shopping()        
