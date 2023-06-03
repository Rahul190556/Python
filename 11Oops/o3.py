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
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item('Phone', 100, 1)
# item2 = Item('Laptop', 1000, 3)
# item3 = Item('Cable', 1005, 5)
# item4 = Item('Mouse', 400, 3)
# item5 = Item('Keyboard', 500, 10)
# print(Item.all)

Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.5)) # O/p:False
print(Item.is_integer(7.0)) # O/p:True



# static methods when you have a function that is related to the class but doesn't require instance or class data,
#  and use class methods when you need to perform operations involving the class itself or manipulate class-level data.