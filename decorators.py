def my_decorator(function):
    def wrapper():
        print("This is before")
        function()
        print("This is After")
    return wrapper

@my_decorator
def hello():
    print("Hello, World!")

hello()