# "Learn about python Enum" by soumilshah1994 on YouTube
from enum import Enum, unique, auto

class Sensor(Enum):
    # below is docstring
    """
    Sensor
    This is enums for Sensors
    """
    
    Temperature = 1
    Humidity = 2
    Air = auto()
    

if __name__ == "__main__":
    print(Sensor)
    print(Sensor.Temperature.name)
    print(Sensor.Temperature.value)
    print(Sensor.Air.value)
    print("\n")
    
    # prints each item in class Sensor
    for item in Sensor:
        print(item.name, "=", item.value)
    print("\n")
    print(Sensor.__doc__) # prints the docstring
    
    
    #################################################
    ##############################################
    ##########################################
    
# 'Enumeration' by NeuralNine
# useful when you want to index data that hasnt already been indexed


mynames = ['John', 'Mike', 'Anna', 'Bob', 'Sara']

# we want to index this list ^^^^^^


# this isn't necessarily a *wrong* way to do it, but it is unnecessarily complicated
counter = 0
for name in mynames:
    print(f'{counter}: {name}')
    counter += 1

# enumeration library makes this easier
for index, name in enumerate(mynames):
    print(f'{index}: {name}')


print(list(enumerate(mynames))) # creates a list of tuples

















