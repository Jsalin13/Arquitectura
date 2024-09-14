class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self):
        title, description = self.view.get_task_details()
        self.model.add_task(title, description)
        self.view.show_message("Tarea agregada exitosamente.")

    def remove_task(self):
        title = self.view.get_task_title()
        self.model.remove_task(title)
        self.view.show_message("Tarea eliminada exitosamente.")

    def complete_task(self):
        title = self.view.get_task_title()
        self.model.complete_task(title)
        self.view.show_message("Tarea marcada como completada.")

    def list_tasks(self):
        tasks = self.model.get_all_tasks()
        self.view.show_tasks(tasks)

    def handle_menu(self):
        while True:
            self.view.show_menu()
            choice = input("Elige una opción:")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.remove_task()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                self.list_tasks()
            elif choice == '5':
                break
            else:
                self.view.show_message("Elección no válida. Por favor inténtalo de nuevo.")
