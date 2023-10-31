from Task import Task
from TaskList import TaskList

if __name__ == "__main__":

    task_list = TaskList()

    while (True):

        print('1. Add task')
        print('2. Remove task')
        print('3. List all tasks')
        print('4. Mark complete/incomplete')
        print('5. Exit')

        choice = int(input())

        if choice == 1:
            title = input("Title: ")
            description = input("Description:")
            status = input("Status: ")
            task = Task(title, description, status)
            task_list.add(task)

        if choice == 2:
            task_number = input("Task number: ")
            task = task_list.list_all_tasks()[task_number]
            task_list.remove(task)

        if choice == 3:
            for i, task in enumerate(task_list.list_all_tasks()):
                print(f"{i}. {task}")

        if choice == 4:
            task_number = int(input("Task number: "))
            task = task_list.list_all_tasks()[task_number]
            if (task.status.lower() == "incomplete"):
                task.mark_complete()
            else:
                task.mark_incomplete()
            
        if choice == 5:
            break
