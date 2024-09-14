class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = 'Completado' if self.completed else 'Tarea no completada'
        return f"Title: {self.title}, Descripción: {self.description}, Status: {status}"


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()

    def get_all_tasks(self):
        return self.tasks
