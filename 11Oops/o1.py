# The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize 
# the object's attributes and serves no other purpose. It is only used within classes.

class Item:

    #magic method
    def __init__(self,name):
        print(f"An instance created:{name}")  #f is format string

    def calculat_total_price(self,x,y):   
        return x*y



item1=Item("Phone")
item1.price=10000
item1.quantity=8
print(item1.calculat_total_price(item1.price,item1.quantity))

item2=Item('washing Machine')
item2.price=15000
item2.quantity=8
print(item1.calculat_total_price(item1.price,item2.quantity))