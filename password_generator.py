import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("Password Generator")


# PyPassword Generator
import random

# Generator function
def generator(number_of_something, string_of_something):
    password = []
    letters = string_of_something
    for i in range(0, number_of_something):
        letters = list(letters)
        num = random.randint(0, len(letters) - 1)
        password.append(letters[num])
    # letters.pop(num)
    password_str = "".join(password)
    return password_str

# Shuffle Function
def shuffle(password_string):
    password_string = list(password_string)
    num1 = random.randint(0, len(password_string) - 1)
    num2 = random.randint(0, len(password_string) - 1)
    # Swaping
    temp = password_string[num1]
    password_string[num1] = password_string[num2]
    password_string[num2] = temp
    password_string = "".join(password_string)
    return password_string

letters_input = customtkinter.CTkEntry(master=app, placeholder_text="How many letters")
letters_input.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
symbols_input = customtkinter.CTkEntry(master=app, placeholder_text="How many symbols")
symbols_input.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
numbers_input = customtkinter.CTkEntry(master=app, placeholder_text="How many numbers")
numbers_input.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
generated_password = customtkinter.CTkLabel(master=app, text="Password")
generated_password.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

def button_function():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_of_letters = int(letters_input.get())
    letters_str = generator(number_of_letters, letters)
    numbers = "0123456789"
    number_of_numbers = int(numbers_input.get())
    numbers_str = generator(number_of_numbers, numbers)
    symbols = "!@#$%^&*()[]<>?/+-"
    number_of_symbols = int(symbols_input.get())
    symbols_str = generator(number_of_symbols, symbols)

    generated_password.configure(text = str(letters_str + numbers_str + symbols_str))

button = customtkinter.CTkButton(master=app, text="Generate", command=button_function)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()