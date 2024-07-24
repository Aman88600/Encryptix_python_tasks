tasks = []

def add_task():
    task = input("Enter the Task : ")
    tasks.append(task)

def show_tasks():
    if len(tasks) == 0:
        print("No tasks eneted yet")
    else :
        count = 0
        for i in tasks:
            count += 1
            print(f"{count} : {i}")

def delete_task():
    task_num = int(input("Enter task number to delete the task : "))
    task_num -= 1
    tasks.pop(task_num)

def main():
    # Loop
    keep_going = 1
    while keep_going == 1:
        
        # No Tasks in the list
        if len(tasks) == 0:
            user_choice = int(input("1 to Add task\n2 to show tasks\nEnter Input : "))
            if user_choice == 1:
                #Add task
                add_task()
            elif user_choice == 2:
                # Show all tasks
                show_tasks()
            else:
                print("Invalid Input : ")
        # Some task or tasks in the list
        else :
            user_choice = int(input("1 to Add task\n2 to show tasks\n3 to delete task\nEnter Input : "))
            if user_choice == 1:
                #Add task
                add_task()
            elif user_choice == 2:
                # Show all tasks
                show_tasks()
            elif user_choice == 3:
                # Delete task
                delete_task()
            else:
                print("Invalid Input : ")
        keep_going = int(input("Press 1 to keep going any other key to stop : "))
if __name__ == "__main__":
    main()