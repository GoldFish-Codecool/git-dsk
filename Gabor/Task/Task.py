class Task:

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    
    def mark_complete(self):
        self.status = "Complete"

            
    def mark_incomplete(self):
        self.status = "Incomplete"


    def __str__(self):
        return f"{self.title}: {self.description} - {self.status}"