# To-Do List Application
task_list = []# Define an empty list to store tasks

# Function to add a task
def add_task_to_list(task):
    task_list.append(task)
    print(f"Task '{task}' added!")

# Function to list all tasks
def list_all_tasks():
    if task_list:
        print("To-Do List:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do List is empty.")

# Function to mark a task as done
def complete_and_remove(task_index):
    if 1 <= task_index <= len(task_list):
        task = task_list[task_index - 1]
        print(f"Task '{task}' is completed!")
        del task_list[task_index - 1]
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Complete the task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task_to_list(task)
    elif choice == "2":
        list_all_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to complete: "))
        complete_and_remove(task_index)
    elif choice == "4":
        print("Goodbye! Have a great day!!!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")