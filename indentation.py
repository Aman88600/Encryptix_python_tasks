# In python indentation is important since, it is used to tell the scope of functions, loops, classes etc.

def my_function():
    print("This is the print statement in the function")

class MyClass:
    def class_function(self):
        print("This print is in the class function")

for i in range(1,11):
    print(f"This print is in a for loop with i  = {i}")

my_function()
obj = MyClass()
obj.class_function()
