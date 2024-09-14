class TaskView:
    def show_tasks(self, tasks):
        if not tasks:
            print("Error en la tarea")
        for task in tasks:
            print(task)

    def show_message(self, message):
        print(message)

    def get_task_details(self):
        title = input("Ingrese el título de la tarea: ")
        description = input("Ingrese la descripción de la tarea: ")
        return title, description

    def get_task_title(self):
        return input("Ingrese el título de la tarea: ")

    def show_menu(self):
        print("\nMenu:")
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Completar Tarea")
        print("4. Listar Tareas")
        print("5. Salir")
