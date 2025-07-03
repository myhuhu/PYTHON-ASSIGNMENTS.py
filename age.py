# Defining a class named 'Person'
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Public method to get the name
    def get_name(self):
        return self.__name

    # Public method to set the name
    def set_name(self, name):
        self.__name = name

    # Public method to get the age
    def get_age(self):
        return self.__age

    # Public method to set the age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Creating an object (instance) of the 'Person' class
person = Person("Alice", 30)

# Accessing and modifying private attributes via public methods
print(person.get_name())  # Output: Alice
person.set_age(31)
print(person.get_age())   # Output: 31

# Attempting to set a negative age
person.set_age(-5)        # Output: Age must be positive
print(person.get_age())   # Output: 31
