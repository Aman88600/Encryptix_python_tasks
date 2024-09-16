def hello(*args):
    for i in args:
        print(i)

hello("Hello", "My", "Name", "is", "Aman")

def myfun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    
myfun(first_name = "Aman", last_name = "Basoya")