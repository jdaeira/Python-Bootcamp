#Simple Function
def greet():
    print("Hello")
    print("I am inside a function")
    print("Functions are fun!")

greet()

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")

greet_with_name("John")

#Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with(name = "John", location = "Hayward")

#Function with keyword arguments
greet_with(location = "Hayward", name = "John")