class Task:
    """Класс задач пользователей"""
    def __init__(self, name_task):
        self.name = name_task
        self.check_box = None

    def __str__(self):
        return self.name

    def yes_check(self):
        self.check_box = 'В работе'
        return self.check_box

    def no_check(self):
        self.check_box = 'Выполнена'
        return self.check_box

