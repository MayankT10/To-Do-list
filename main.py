from greet import greet_art

tasks = []

def add_task():
    task = input("Enter a new task:")
    tasks.append(task)
    print("Task added succesfully.")

def view_task():
    print("The tasks are ",tasks)
    
def delete_task():
    pass

def main():
    print(greet_art)
    print('''
1.Add Task
2.Delete task
3.View tasks
4.Quit
''')
    choice = input("Enter your choice:")
    if choice == "1":
        add_task()
        main()
    elif choice == "2":
        delete_task()
        main()
    elif choice == "3":
        view_task()
        main()
    elif choice == "4":
        print("Closing..")
        pass
    else:
        print("Enter a valid choice.")



if __name__ == "__main__":
    main()