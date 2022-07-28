# https://www.youtube.com/watch?v=QrzHImDEq_w

# type annotation when assigning value to variable
hello: str = "hello world"
# same as this:
hello = "hello world"

def add(x: int, y: int):
    return x + y

new_val: int = add(4,5)

# type annotations allows the IDE to warn us if something doesn't look right
# this doesn't seem to work in Spyder though >.> also cant get it to warn me in
# VS Code either... maybe settings need to be changed?
new_val: int = add("four", "five") # IDE should warn us here

str_int = {'one': 5, 'two': 7}
int_int = {1: 5, 2: 7}

def sum_dict(var: dict[str, int]) -> int: # expecting to return int. in dictionary,
                                        # expecting key to be str and value to be int
                                        # (see the types in list)
    return sum(var[key] for key in var.keys())

sum_dict(str_int)
sum_dict(int_int)

# union operator
from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]: # takes integer OR float, and we expect it to return either of those
    return x + y

new_val: Union[int, float] = add(4.5, 5.5)


# casting
from typing import cast

