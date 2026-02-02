class User:
    """ Класс пользователй"""
    def __init__(self, personnel_number, name):
        self.personnel_number = personnel_number
        self.name = name

    def __str__(self):
        return f"User: {self.name}, Personnel Number: {self.personnel_number}"

    def get_personnel_number(self):
        return self.personnel_number
