# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

# Function to display tasks
def display_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to display.")

# Function to remove a task
def remove_task():
    display_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to remove.")

# Main loop
while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
