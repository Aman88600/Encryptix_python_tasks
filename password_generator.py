import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("Password Generator")


# # Number 1
# number_1_entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter Number 1")
# number_1_entry.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


# # Number 2
# number_2_entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter Number 2")
# number_2_entry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

# # Operation
# operation = customtkinter.CTkEntry(master=app, placeholder_text="Enter Operation")
# operation.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# # Output
# output = customtkinter.CTkLabel(master=app, text="Output")
# output.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


def button_function():
    print("Button Clicked")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Generate", command=button_function)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()