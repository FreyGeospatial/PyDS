from itertools import groupby
  
# create a class  
class Person:
    def __init__(self, fname: str, lname: str, id: int):
        self.firstname: str=fname
        self.lastname: str=lname
        self.id: int=id
  
# Key function by which we will sort and group
key_func = lambda x: x.lastname
  
p1 = Person('John', 'Smith', 1)
p2 = Person('Lacey', 'Smith', 2)
p3 = Person('Sally', 'Lane', 3)
p4 = Person('Jim', 'Drake', 4)

people = [p1, p2, p3, p4]

my_group = groupby(sorted(people, key=key_func), key=key_func)

l = list(my_group)

