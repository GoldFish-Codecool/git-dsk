#Todo List Application: Design a simple command-line To-Do list where users can add tasks, mark them as done, and list all tasks. (Advanced: Save tasks to a file so they persist between sessions.)

tasks = []

def addtask(task):
  tasks.append(task)
  print(f"\nTask \"{task}\" added!")

def modtask(task_index):
  if 0 <= task_index <= len(tasks):
    tasks[task_index] = "[Done] " + tasks[task_index]
    print (f"\nTask \"{task}\" marked as done!")
  else:
    print ("\nInvalid task!")

def tasklist():
  print("\nAdded tasks:")
  for index, task in enumerate(tasks):
    print(f"{index+1}. {task}")

def quittask():
  print("\nExiting. See you later!")

print("\nWelcome to the task manager!")

while True:
  print("\nOptions - please select number:")
  print("1. - Add new task.")
  print("2. - Mark task as \"Done\".")
  print("3. - List tasks.")
  print("4. - Exit")

  whattodo = input ("\nWhat to do? (1-2-3-4):  ")
  if whattodo == "1":
    task = input ("\nPlease specify task: ")
    addtask(task)
  elif whattodo == "2": 
    tasklist()
    task_index = int(input("\nWhich is done? Please provide task number: ")) - 1
    modtask(task_index)
  elif whattodo == "3":
    tasklist() 
  elif whattodo == "4":
    quittask
    break
  else:
    print("\nInvalid choice. Try again.")
  
