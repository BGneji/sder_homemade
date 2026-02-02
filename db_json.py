import json
import os


class DB_connection:
    def __init__(self, db):
        self.db = db

    def __str__(self):
        return self.db

    def read_db(self):
        try:
            if os.path.exists(self.db):
                with open(self.db, 'r', encoding='utf-8') as json_file:
                    return json.load(json_file)
            return []
        except FileNotFoundError:
            print(f"Файл {self.db} не найден.")
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON.")

    def write_db(self, new_data):
        existing_data = self.read_db()
        for user in existing_data:
            if new_data.get('id') == user['id'] and user['имя'] == new_data.get('имя'):
                for i in user['tasks']:
                    task_key = list(new_data['tasks'].keys())[0]
                    if list(i.keys())[0] == task_key:
                        print('Такая задача уже есть')
                        return
                else:
                    user['tasks'].append(new_data.get('tasks'))
                    print("Задача добавлена")
                    break
        with open(self.db, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

    def get_user(self, personnel_number, name):
        for user in self.read_db():
            if user['id'] == personnel_number:
                if user['id'] == personnel_number and user['имя'] == name:
                    print('Вы успешно вошли в аккаунт')
                    return user
        return None

    def add_user(self, personnel_number, name):
        if self.get_user(personnel_number, name) is None:
            new_user = {
                'id': personnel_number,
                'имя': name,
                'tasks': []
            }
            existing_data = self.read_db()
            existing_data.append(new_user)
            with open(self.db, 'w', encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
                print('Регистрация прошла успешно')
        elif not self.get_user(personnel_number, name):
            print('Такой табельный номер уже есть')
        else:
            print('Такого пользователь уже есть')

    def dell_task_db(self, old_data):
        existing_data = self.read_db()
        for user in existing_data:
            if old_data.get('id') == user['id'] and user['имя'] == old_data.get('имя'):
                for i in user['tasks']:
                    if list(i.keys())[0] == list(old_data['tasks'].keys())[0]:
                        print(list(old_data['tasks'].keys())[0])
                        key_to_remove = list(old_data['tasks'].keys())[0]
                        print(user['tasks'])
                        user['tasks'] = [task for task in user['tasks'] if key_to_remove not in task]
                        print("Задача удалена")
                        break
                else:
                    print('Такой задачи нет')
            with open(self.db, 'w', encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

    def write_db_task(self, new_data):
        existing_data = self.read_db()
        for user in existing_data:
            if new_data.get('id') == user['id'] and user['имя'] == new_data.get('имя'):
                for i in user['tasks']:
                    task_key = list(new_data['tasks'].keys())[0]
                    if list(i.keys())[0] == task_key:
                        i[task_key] = new_data['tasks'][task_key]
                        print(f"Обновлено: {task_key} = {new_data['tasks'][task_key]}")
                        break
        with open(self.db, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
