# main.py
from model.task_model import TaskModel
from view.task_view import TaskView
from controller.task_controller import TaskController

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)
    controller.handle_menu()

if __name__ == "__main__":
    main()
