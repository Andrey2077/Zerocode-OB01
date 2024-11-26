# Менеджер задач
#
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
from datetime import datetime


class Task:
    list_of_tasks = []

    def __init__(self, description = "", date_of_ending = datetime.min, status = False):
        self.description = description
        self.date_of_ending = date_of_ending
        self.status = status


    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_description(self):
        return self.description

    def add_task(self):
        Task.list_of_tasks.append(self)

    @classmethod
    def print_notdone_tasks(cls):
        for task in Task.list_of_tasks:
            if task.get_status() == False:
                print(f"{task.get_description()}")


task_one = Task("Первая задача")
Task.list_of_tasks.append(task_one)
task_two = Task("Вторая задача")
Task.list_of_tasks.append(task_two)
task_three = Task("Третья задача")
Task.list_of_tasks.append(task_three)
task_four = Task("Четвертая задача")
Task.list_of_tasks.append(task_four)
task_five = Task("Пятая задача")
Task.list_of_tasks.append(task_five)
task_four.set_status(True)
Task.print_notdone_tasks()


