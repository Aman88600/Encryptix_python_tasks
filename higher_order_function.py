# Higher order functionm taking other function as input
def greet(func):
    greeting = func("Hello")
    print(greeting)

def hello(my_string):
    return my_string

greet(hello)
