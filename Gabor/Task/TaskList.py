from Task import Task

class TaskList:

    def __init__(self):
        self.task_list = []


    def add(self, task):
        self.task_list.append(task)

    
    def remove(self, task):
        self.task_list.remove(task)


    def list_all_tasks(self) -> list[Task]:
        return self.task_list