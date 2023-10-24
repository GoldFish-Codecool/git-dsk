#**Todo List Application**:
# - Design a simple command-line To-Do list where users can add tasks, mark them as done, and list all tasks. (Advanced: Save tasks to a file so they persist between sessions.)

import sys

todo_entry = sys.argv[1]
file_name = "Tamas_todo_list.txt"

with open(file_name, "a") as file:
  file.write(todo_entry + "\n")

with open(file_name, "r") as file:  
  content = file.read()
  print ("\n\n Here is your full list: \n\n", content)

done = input ("Do you want to mark any of them as done? (Y/N) ")
done = done.upper()

if done == "Y" :
  done_entry = input ("Which one? ")
  with open(file_name, "r") as file:
    content = file.read()
    modified_content = content.replace (done_entry, done_entry + "== DONE ==")

  with open(file_name, "w") as file:
    file.write(modified_content)

  with open(file_name, "r") as file:
    content = file.read()
    print ("\n\n Here is your full list: \n\n", content)
else :
  print ("Ok, thank you for using the To-Do list application.")