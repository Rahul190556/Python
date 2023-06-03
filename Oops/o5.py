#class inheritence
# Inheritance allows us to define a class that inherits all the methods and properties from another class. 
# Parent class is the class being inherited from, also called base class. Child class is the class that inherits 
# from another class, also called derived class.

import csv
class Item:
    
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []  # List to store all items

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations on the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self Object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):   
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):  #cls argument passes the class
        with open("Oops/items.csv",'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)

        for item in items:
            print(item)        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        #we will count out the floats that are point zero
        if isinstance(num,float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self):  #reperesnting your object
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0,broken_phones=0):
        #  call to super function to have access to all attributes/methods present in item
        #  class that will save copy pasting the init method present in item class
        super().__init__(
            name,price,quantity
        )
    # Run validations on the received arguments
        # assert price >= 0, f"Price {price} is not greater than zero!"
        # assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        assert broken_phones >=0, f"Broken_phone {broken_phones} is not greater than zero"

    # # Assign to self Object
    #     self.name = name
    #     self.price = price
    #     self.quantity = quantity
        self.broken_phones=broken_phones



phone1=Phone("jscPhonev10",500,5,1)
print(phone1.calculate_total_price())
phone2=Phone("jscPhonev20",700,5,1)
print(Item.all)
print(Phone.all)