to_do_list = []

def add_task():
    task = input("Enter the Task : ")
    to_do_list.append(task)

def main():
    # Loop
    keep_going = 1
    while keep_going == 1:
        #Add task
        add_task()
        print(to_do_list)

        keep_going = int(input("Press 1 to keep going any other key to stop : "))
if __name__ == "__main__":
    main()