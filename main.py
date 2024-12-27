from greet import greet_art
import json


tasks = []

def add_task():
    task = input("Enter a new task:")
    tasks.append(task)
    print("Task added succesfully.")

def view_task():
    # if not tasks:
    #     print("Your task list is empty")
    # else :
    #     print("\n=== Your Tasks ===")
    #     for i, task in enumerate(tasks,1):
    #         if task['completed']:
    #             status ="✓"
    #         else:
    #             status ="✗"
    #         print(f"{i}.{task['name']} [{status}]")

    # if len(tasks) == 0:
    #     print("Your task list is empty")
    # else:
    #     print("List of tasks")
    #     for i, tasks in enumerate(tasks):
    #         print(f"{i+1}. {tasks}")
    
    print("The tasks are:")
    for task in tasks:
        print(task)

    # print("The tasks are ",tasks)
    
def delete_task():
    # view_task()
    # delete_num = input("Which task number you want to delete:")
    # int_delete_num = int(delete_num) 
    # if int_delete_num in tasks:
    #     del tasks[int_delete_num]
    #     print("Task has been deleted succesfully")
    # else:
    #     print("Enter a valid task number")
    print("Tasks")
    for i, task in enumerate(tasks):
        print(f"{i+1}.{task}")
    choice = int(input("Enter the number of task that you want to delete:"))

    if 0<choice<=len(tasks):
        del tasks[choice-1]
        print("Task deleted succesfully")
    else: 
        print("Invalid task number")


def menu():
    print("\n1.Return to menu\n2.Quit")
    menu_choice = input("Enter your choice:")
    if menu_choice == "1":
        main()
    elif menu_choice == "2":
        quit()
    else:
        print("Enter a valid choice")
        menu()


# Function to write added tasks only to text file
# def write_tasks():
#     with open("tasks.txt","w") as task_file:
#         for task in tasks:
#             task_file.write(f"{task['name']}|{task['completed']}\n")
#     print("Task saved succesfully")


def save_tasks():
    with open("tasks.json","w") as task_json:
        json.dump(tasks,task_json)
    print("Task saved succesfully")

# def operation():
#   print('''
# 1.Add Task
# 2.Delete task
# 3.View tasks
# 4.Quit
# ''')
#     choice = input("Enter your choice:")


print(greet_art)

def main():
    # print(greet_art)
    # print("To do list")
    print('''
1.Add Task
2.Delete task
3.View tasks
4.Quit
''')
    choice = input("Enter your choice:")
    if choice == "1":
        add_task()
        menu()
        # operation()
    elif choice == "2":
        delete_task()
        menu()
    elif choice == "3":
        view_task()
        menu()
    elif choice == "4":
        print("Closing..")
        pass
    else:
        print("Enter a valid choice.")
        main()



if __name__ == "__main__":
    main()