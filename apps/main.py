import sys
import os
# Путь к родительскому каталогу в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apps.project import Project
from apps.contract import Contract
from apps.database import DataEntry

from utilss.validatee import (
    check_project,
    check_contract,
)
from utilss.interface import (
    contract_menu,
    project_menu)

proj_list = []
contr_list = []

if __name__ == '__main__':
    while True:
        project_menu()
        choice = int(input('Выберите вариант: '))
        list_contract = check_contract()    # Список контрактов для проверки
        list_project = check_project()      # Список проектов для проверки
        data = DataEntry()

        # _________________________________________________
        if choice == 1:                 # Создать проект
            word = input('enter name of project: ')
            if word in list_project:
                print('этот проект уже существует, попробуйте другой')
                continue
            project = Project(word)
            proj_list.append(project)
            # data.create_project(project)
        # _________________________________________________
        elif choice == 2:               # Добавить договор
            contract_menu()
            answer = int(input('enter answer: '))
            # ____________________________________
            if answer == 1:
                word = input('enter name of contract: ')
                # ____________________________________
                if word in check_contract():
                    print('this contract exist')
                    print('do you want continue 1 yes, 0 no: ')
                    answer = int(input('enter answer: '))
                    if answer == 1:
                        continue
                    else:
                        break
                # ____________________________________
                con = Contract(word)
                contr_list.append(con)
                # data.create_contract(contract)
            # elif answer == 2:
            #     for contr in contr_list:
            #         data.create_contract(contr)

        # _________________________________________________
        if choice == 3:                 # Завершить договор
            word = input('enter name of project: ')
            project = Project(word)
            # data.create_project(project)
        # _________________________________________________
        elif choice == 4:               # Список контрактов
            answer = int(input('Контракт=1 Проект=0: '))
            if answer == 1:
                for dat in data.get_contract():
                    print(f'id {dat[0]}   name {dat[1]}     date {dat[2]}')
            elif answer == 0:
                for dat in data.get_project():
                    print(f'id {dat[0]}   name {dat[1]}     date {dat[2]}')
        # _________________________________________________
        elif choice == 5:              # Вернуться к началу
            continue
        # _________________________________________________
        elif choice == 6:              # Завершить и выйти
            break
        # _________________________________________________
        elif choice == 7:              # Завершить
            print('i am here in 7')
            for proj in proj_list:
                data.create_project(proj)
            for contr in contr_list:
                data.create_contract(contr)


























"""
class ManagementSystem:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('db/projects_contracts.db')
        self.curs = self.conn.cursor()

        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS contracts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT,
                sign_date TEXT,
                status TEXT,
                project_id INTEGER)''')

        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT)''')

        self.conn.commit()

    def create_contract(self):
        name = input('Введите название договора: ')
        contract = Contract(name)
        self.curs.execute('INSERT INTO contracts (name, creation_date, status) VALUES (?, ?, ?)',
                            (contract.name, contract.create_date, contract.status))
        self.conn.commit()
        print('Договор создан.')

    def create_project(self):
        name = input('Введите название проекта: ')
        project = Project(name)
        self.curs.execute('INSERT INTO projects (name, creation_date) VALUES (?, ?)',
                            (project.name, project.create_date))
        self.conn.commit()
        print('Проект создан.')

    def close(self):
        self.conn.close()



if __name__ == '__main__':
    
    system = ManagementSystem()
    
    while True:
        print()
        print('1. Создать договор')
        print()
        print('2. Создать проект')
        print()
        print('3. Завершить')
        print()
        choice = input('Выберите вариант: ')

        if choice == '1':
            system.create_contract()

        elif choice == '2':
            system.create_project()

        elif choice == '3':
            system.close()
            break
"""






































# def create_project():
#     while True:
#         print()
#         print('Проект\n'
#             '\n'
#             '1-Создать\n'
#             '2-Добавить договор(с выбором проекта, в который добавлять)\n'
#             '3-Завершить договор(с выбором проекта и договора для завершения)\n'
#             '4-посмотреть список проектов\n'

#             '5-выйти')
#         print()

#         # _______________________________________
#         res = int(input('Выберите вариант: '))
#         if res == 1:
#             print(1)
#         elif res == 2:
#             create_contract2()
#         elif res == 3:
#             print(res)
#         elif res == 4:
#             break
        
#         elif res > 5:
#             print()
#             print()
#             print()

#             print('***enter correct number***')

#             print()
#             print()
#             print()

#         # _______________________________________

# def create_contract2():
#     while True:
#         word = int(input('enter number: '))
#         id = input('id: ')
#         name = input('enter name: ')
#         age = input('age: ')
#         print()
#         print('Договор\n'
#             '\n'
#             '1-Создать\n'
#             '2-Подтвердить договор(с выбором проекта, в который добавлять)\n'
#             '3-Завершить договор(с выбором проекта и договора для завершения)\n'
#             '4-посмотреть список договоров\n'
#             '5-выйти')
#         print()

#         if word == 1:
#             add_contract(id, age, name)





# # print(get_data())
# create_project()








'''

Приблизительный интерфейс может выглядеть так
1. Проект
-Создать
-Добавить договор(с выбором проекта, в который добавлять)
-Завершить договор(с выбором проекта и договора для завершения)

2.Договор
- Создать
-Подтвердить договор(с выбором договора для подтверждения)
-Завершить договор(с выбором договора для завершения)
3. Завершить работу с программой


'''



    
'''
class MainCo:
    def __init__(self, name) -> None:
        self.name = name

    # @staticmethod
    def create_project(self):
        while True:

            print('Проект\n'
                '\n'
                '1-Создать\n'
                '2-Добавить договор(с выбором проекта, в который добавлять)\n'
                '3-Завершить договор(с выбором проекта и договора для завершения)')
            print()

            # _______________________________________
            res = int(input('Выберите вариант: '))
            if res == 1:
                print(self.name)
                new_project = Project(self.name)
                return new_project
            
            if res == 2:
                return(2)
            if res == 3:
                return f'{res} done'
            if res == 4:
                print(help(MainCo.create_project()))
            else:
                print('enter correct number')
            # _______________________________________
'''
    