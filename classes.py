class Student:
    def __init__(self):
        self.__name = "Empty"
        self.__age = 0

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age


aman = Student()
print(aman.get_age())
print(aman.get_name())
