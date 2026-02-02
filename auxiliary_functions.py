def input_user():
    """Получение табельного номера и имя от пользователя"""
    personnel_number = int(input('Введите табельный номер: '))
    name = input('Введите имя: ').capitalize()
    return [personnel_number, name]


def add_dell_execute():
    print('С начало надо войти в аккаунт')
