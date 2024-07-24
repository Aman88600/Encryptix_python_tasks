import customtkinter
import os
from PIL import Image

tasks = []

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Remove", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.title("To Do List")
        self.geometry("400x300")

        # Create entry widget for adding tasks
        self.task_entry = customtkinter.CTkEntry(self, placeholder_text="Enter the Task")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Create button to add tasks
        self.add_task_button = customtkinter.CTkButton(self, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        # Create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Load initial tasks if any
        for task in tasks:
            self.scrollable_label_button_frame.add_item(task, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "test_images", "chat_light.png"))))

    def add_task(self):
        task = self.task_entry.get()
        if task:
            tasks.append(task)
            self.scrollable_label_button_frame.add_item(task)
            self.task_entry.delete(0, customtkinter.END)

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")
        if item in tasks:
            tasks.remove(item)
            self.scrollable_label_button_frame.remove_item(item)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()
