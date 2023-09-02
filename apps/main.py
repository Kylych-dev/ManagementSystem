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

