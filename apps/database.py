import sqlite3


class DataEntry:
    def __init__(self):
        self.conn = sqlite3.connect('db/projects_contracts.db')
        self.curs = self.conn.cursor()

        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS contracts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT,
                sign_date TEXT,
                status TEXT,
                project_id INTEGER,
                FOREIGN KEY (project_id) REFERENCES projects (id))''')

        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT)''')
        self.conn.commit()

    def create_contract(self, data):    # Создание контракта
        self.curs.execute('INSERT INTO contracts (name, creation_date, status) VALUES (?, ?, ?)',
                            (data.name, data.create_date, data.status))
        self.conn.commit()
        print('Договор создан.')

    def create_project(self, data):     # Создание проекта
        self.curs.execute('INSERT INTO projects (name, creation_date) VALUES (?, ?)',
                            (data.name, data.create_date))
        self.conn.commit()
        print('Проект создан.')

    def update_contract_status(self, contract_id, new_status):
        # Изменение статуса
        self.curs.execute('UPDATE contracts SET status = ? WHERE id = ?',
                          (new_status, contract_id))
        self.conn.commit()
        print(f'Статус договора с id {contract_id} обновлен.')

    def get_project(self):
        # Получить список проектов
        self.curs.execute('SELECT id, name, creation_date FROM projects')
        rows = self.curs.fetchall()

        list_projects = []
        for row in rows:
            project_id, project_name, project_description = row  # (1, 'Project A', 'Description for Project A') its row
            list_projects.append(row)    
        # return f"Project ID: {project_id}, Name: {project_name}, Description: {project_description}"
        return list_projects
    
    def get_contract(self):
        # Получить список контрактов
        self.curs.execute('SELECT id, name, creation_date FROM contracts')
        rows = self.curs.fetchall()

        list_contracts = []
        for row in rows:
            project_id, project_name, project_description = row  # (1, 'Project A', 'Description for Project A') its row
            list_contracts.append(row)    
        # return f"Project ID: {project_id}, Name: {project_name}, Description: {project_description}"
        return list_contracts

    def close(self):
        # Закрываем соединение
        self.conn.close()

