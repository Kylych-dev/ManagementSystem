# Documentation Management System

## Welcome to My Project! 
Это удивительное консольное приложение которое делает что-то очень полезное на Python 3+ для<br> 
управления проектами и договорами. Оно использует объектно-ориентированный подход и базу<br>
данных для хранения информации. Добавление договора к проекту - это просто, как добавление<br>
сахара в чашку чая. Важно помнить, что мы не поддерживаем добавление черновых договоров.<br>
Приложение ещё не закончено и продолжаю работу над ней.<br>

## Структура проекта

| Папка    | Содержимое                        |
|----------|-----------------------------------|
| `apps`   | contract, database, main, project |
| `db`     | data2, projects_contracts.db      |
| `utilss` | interface, validatee              |
| `___`    | ___                               |
| `___`    | ___                               |
| `___`    | ___                               |

 tree -I 'venv|__pycache__|*.pyc|*.pyo|*.pyd'<br>
.<br>
├── apps<br>
│   ├── contract.py<br>
│   ├── database.py<br>
│   ├── main.py<br>
│   └── project.py<br>
├── db<br>
│   ├── data2.py<br>
│   └── projects_contracts.db<br>
├── README.md<br>
└── utilss<br>
    ├── interface.py<br>
    └── validatee.py<br>


# Список доступных действий:<br>
Проект<br>
- Создать<br>
- Добавить договор(с выбором проекта, в который добавлять)<br>
- Завершить договор(с выбором проекта и договора для завершения)<br>

Договор<br>
- Создать<br>
- Подтвердить договор(с выбором договора для подтверждения)<br>
- Завершить договор(с выбором договора для завершения)<br>
- Завершить работу с программой<br>


## Требования

Для запуска проекта вам потребуется Python версии 3.x. 

## Установка и запуск

1. Склонируйте репозиторий на свой компьютер:

    + ***git clone https://github.com/yourusername/my-project.git***

2. Перейдите в каталог проекта:

   + ***cd ManagementSystem***

3. Создайте виртуальную среду (рекомендуется):

   + ***python -m venv venv***

4. Активируйте виртуальную среду:
   
   + ***source venv/bin/activate***

5. Запустите приложение:

   + ***python3 apps/main.py***


## Contributing

* Мирбеков Кылыч
* Электронная почта: mirbekov1kylych@gmail.com
* GitHub: [https://github.com/kylych-dev](https://github.com/kylych-dev)
* GitLab: [https://gitlab.com/kylych-dev](https://gitlab.com/kylych-dev)
* telegram: @mirbekov0909