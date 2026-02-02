from Task import Task
from auxiliary_functions import input_user, add_dell_execute
from db_json import DB_connection
from User import User


class Job:
    def __init__(self):
        self.current_user = False
        self.data_json = {}
        self.data = []

    def __str__(self):
        return self.current_user

    def status_current_user(self):
        print(self.current_user)
        print(self.data)
        print(self.data_json)

    def sing_in(self, personnel_number, name):

        """Вход в аккаунт"""
        sing_in_user = db.get_user(personnel_number, name)
        if sing_in_user is not None:
            self.current_user = True
            self.data_json['id'] = personnel_number
            self.data_json['имя'] = name
            self.data.append(personnel_number)
            self.data.append(name)
            self.data.append(self.current_user)
        else:
            print('Такого пользователя нет')
            key = input("Пользователь с таким именем не найден, хотите зарегистрироваться y/n? ")
            if key == 'y' or key == 'н':
                user_data = input_user()
                user = User(user_data[0], user_data[1])
                db.add_user(user.personnel_number, user.name)

    def sing_out(self):
        """Выход из аккаунта"""
        self.data_json = {}
        self.data = []
        self.current_user = False

    def add_task(self, tsk_name):
        self.data_json['tasks'] = {str(tsk_name.name).capitalize().strip(): 'None'}
        db.write_db(self.data_json)

    def dell_task(self, tsk_name):
        self.data_json['tasks'] = {str(tsk_name.name).capitalize().strip(): 'None'}
        db.dell_task_db(self.data_json)

    def get_tasks(self):
        all_user = db.read_db()
        print(f'Список задач {self.data_json.get('имя')}')

        for user in all_user:
            self.data_json.get('имя')
            if self.data_json.get('id') == user['id'] and user['имя'] == self.data_json.get('имя'):
                for task in user['tasks']:
                    print(task)

    def check_task(self, tsk_name, task_status):
        all_user = db.read_db()
        for user in all_user:
            self.data_json.get('имя')

            if self.data_json.get('id') == user['id'] and user['имя'] == self.data_json.get('имя'):
                for task_user in user['tasks']:
                    if tsk_name.name in task_user:
                        if 1 == task_status:
                            self.data_json['tasks'] = {str(tsk_name.name).capitalize().strip(): tsk_name.yes_check()}
                        elif 2 == task_status:
                            self.data_json['tasks'] = {str(tsk_name.name).capitalize().strip(): tsk_name.no_check()}
                db.write_db_task(self.data_json)
            print(self.data_json)

    def user_all(self):
        get_db = db.read_db()
        print('*'*10)
        for use_id_name in get_db:
            print(f'Табельный номер: {use_id_name['id']} Имя пользователя: {use_id_name['имя']}')
        print('*'*10)


database_path = './data.json'
db = DB_connection(db=database_path)
jod_program = Job()

if __name__ == '__main__':

    while True:
        try:
            print()
            print("Вы находитесь в приложении списка дел"
                  "\nЧто вы хотите сделать?"
                  "\n\t1. Войти в аккаунт."
                  "\n\t2. Выйти из аккаунта."
                  "\n\t3. Зарегистрироваться."
                  "\n\t4. Добавить задачу."
                  "\n\t5. Удалить задачу."
                  "\n\t6. Отметить задачу выполненной."
                  "\n\t7. Получить список задача."
                  "\n\t8. Получить список пользователей."
                  "\n\t9. Выйти из программы."
                  "\n\t10. Тест данных")

            while True:
                flag = input('Введите цифру: ')
                if flag.isdigit():
                    flag = int(flag)
                    break
                else:
                    print('Вы ввели букву или нечего, а нужно число')

            if flag == 1:
                """Войти в аккаунт"""
                user_data = input_user()
                user = User(user_data[0], user_data[1])
                jod_program.sing_in(user.personnel_number, user.name)

            elif flag == 2:
                """Выйти из аккаунта"""
                jod_program.sing_out()
                print('Вы успешно вышли из аккаунта')

            elif flag == 3:
                """Регистрация"""
                user_data = input_user()
                user = User(user_data[0], user_data[1])
                db.add_user(user.personnel_number, user.name)

            elif flag == 4:
                """Добавить задачу"""
                if jod_program.current_user is False:
                    add_dell_execute()
                else:
                    name_task = input('Введите название задачи для добавления: ')
                    if isinstance(name_task, str) and name_task.isdigit():
                        print('Название задачи не может содержать только цифры ')
                    else:
                        tsk = Task(name_task)
                        jod_program.add_task(tsk)
            elif flag == 5:
                """Удалить задачу"""
                if jod_program.current_user is False:
                    add_dell_execute()
                else:
                    name_task = input('Введите название задачи для удаления: ')
                    tsk = Task(name_task)
                    jod_program.dell_task(tsk)
            elif flag == 6:
                """ Изменить статус задачи """
                if jod_program.current_user is False:
                    add_dell_execute()
                else:
                    name_task = input('Введите название задачи для изменения статуса: ')
                    print(
                        "\n\t1. В работе"
                        "\n\t2. Выполнена"
                    )
                    status_task = int(input('Введите статуса задачи: '))
                    tsk = Task(name_task)
                    jod_program.check_task(tsk, status_task)
            elif flag == 7:
                """Получить список задача"""
                if jod_program.current_user is False:
                    add_dell_execute()
                else:
                    jod_program.get_tasks()
            elif flag == 8:
                """Получить список пользователей"""
                jod_program.user_all()
            elif flag == 9:
                print('Завершение работы программы')
                break
            elif flag == 10:
                """Тест программы"""
                jod_program.status_current_user()
                list_db = db.read_db()
                print()
                print('*' * 10)
                for i, row in enumerate(list_db):
                    print(i)
                    print(list_db[i])
        except Exception as e:
            print(f'Произошла ошибка: {e}')
