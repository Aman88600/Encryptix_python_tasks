# Tries to do something
try:
    a = 10/0
    print(a)
# If exception arise then, this block catches it
except ZeroDivisionError:
    print("Cannot divide by 0")
# This block will run wheather exception occurs or not
finally:
    print("This is the end of program")