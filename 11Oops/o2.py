class Item:
    
    pay_rate=0.8 # The pay rate after 20% discount

    #magic method
    def __init__(self,name:str,price:float,quantity=0):
       #Run validations to the received arguments
       assert price >=0,f"Price{price} is not greater than zero!"
       assert quantity>=0,f"Qunatitiy {quantity} is not greater than zero"

       self.name=name
       self.price=price
       self.qunatity=quantity

    def calculate_total_price(self):   
        return self.price*self.qunatity
    
    def apply_discount(self):
        self.price=self.price * self.pay_rate
        



item1=Item("Phone",10000,5)

item2=Item('washing Machine',15000,8)
# item3=Item("watch",8000,-1)

print(item1.name,item2.price,item1.calculate_total_price())
print(Item.__dict__) # All the attrtibute for class level
print(item1.__dict__) # All the attrtibute for instance level

item1.apply_discount()
print(item1.price)
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)