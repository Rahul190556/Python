import csv

class Item:
    
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []  # List to store all items

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations on the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"


        # Assign to self Object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    #property Decorator = Read-Only Atrritbutes Like private keyword in c++
    def name(self):
        return self.__name
    
    @name.setter
    #it helps to change the name if user want to change
    def name(self,value):
        if len(value)>10:
            raise Exception("The name is too long!")
        print("You are trying to change name")
        self.__name=value

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

    def __connect(self,smpt_server):
        pass
    def __prepare_body(self):
        return f"""
        Hello Someone.
        we have {self.name},{self.quantity} times.
        Regarding, Rahul
        """
    def __send(self):
        pass
    def send_email(self):
        self.__connect('')
        return self.__prepare_body()
        self.__send()


    def __repr__(self):  #reperesnting your object
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    