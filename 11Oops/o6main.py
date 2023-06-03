from o6Item import Item
from o6phone import Phone

Item1=Item("MyItem",750)
Item1.name="newItem"
print(Item1.name)


#abstraction
# Hiding unnecessary information from instances
print(Item1.send_email())

# The word "polymorphism" means "many forms", and in programming it refers to 
# methods/functions/operators with the same name that can be executed on many objects or classes.