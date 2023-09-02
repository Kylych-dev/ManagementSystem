import sqlite3
from utilss.validatee import check_contract 


def create_contract():
    with sqlite3.connect('db/projects_contracts.db') as db:
        cur = db.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT)''')        
        db.commit()

def add_contract(id, name, age):
    conn = sqlite3.connect('db/projects_contracts.db')
    cur = conn.cursor()
    data = id, name, age

    cur.execute('INSERT INTO contracts (id, name, description) VALUES (?, ?)', data)
    
    conn.commit()
    conn.close()


def add_project(id, name, age):
    conn = sqlite3.connect('db/projects_contracts.db')
    cur = conn.cursor()
    data = id, name, age

    cur.execute('INSERT INTO projects (id, name, description) VALUES (?, ?)', data)
    
    conn.commit()
    conn.close()


def show_project():
    with sqlite3.connect('db/projects_contracts.db') as db:
        cur = db.cursor()
        # cur.execute('''
        #     CREATE TABLE IF NOT EXISTS projects (
        #         id INTEGER PRIMARY KEY,
        #         name TEXT,
        #         creation_date TEXT)''')
        

        # data = id, name, age
        # cur.execute('INSERT INTO projects (id, name, description) VALUES (?, ?)', data)

        cur.execute('SELECT * FROM contracts WHERE status = "активен"')
        active_contracts = cur.fetchall()
        return active_contracts




        # db.commit()
        # db.close()





"""
conn = sqlite3.connect('db/projects_contracts.db')
cur = conn.cursor()

# Создаем таблицу, если она еще не существует projects
cur.execute('''CREATE TABLE IF NOT EXISTS contracts 
            (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

# Пример вставки данных
project_data = ('tiffany', 'dallas')

cur.execute('INSERT INTO projects (name, description) VALUES (?, ?)', project_data)

# Фиксируем изменения и закрываем соединение
conn.commit()
conn.close()


CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY, 
                    title TEXT, 
                    date 
                    description TEXT)''')
                    
                    


def create_contract(self, contract):
    self.curs.execute('INSERT INTO contracts (name, creation_date, status) VALUES (?, ?, ?)',
                      (contract.name, contract.create_date, contract.status))
    self.conn.commit()
    print('Договор создан.')

def create_project(self, project):
    self.curs.execute('INSERT INTO projects (name, creation_date) VALUES (?, ?)',
                      (project.name, project.create_date))
    self.conn.commit()
    print('Проект создан.')

def update_contract_status(self, contract_id, new_status):
    # Изменение статуса
    self.curs.execute('UPDATE contracts SET status = ? WHERE id = ?', 
                        (new_status, contract_id))
    self.conn.commit()
    print(f'Статус договора с id {contract_id} обновлен.')

def get_projects(self):
    # Получить список проектов
    self.curs.execute('SELECT id, name, creation_date FROM projects')
    rows = self.curs.fetchall()

    list_projects = []
    for row in rows:
        project_id, project_name, project_creation_date = row
        project = Project(project_name, create_date=project_creation_date)
        list_projects.append(project)
    
    return list_projects

def get_contracts(self):
    # Получить список контрактов
    self.curs.execute('SELECT id, name, creation_date, sign_date, status, project_id FROM contracts')
    rows = self.curs.fetchall()

    list_contracts = []
    for row in rows:
        contract_id, contract_name, contract_creation_date, contract_sign_date, contract_status, project_id = row
        contract = Contract(contract_name)
        contract.create_date = contract_creation_date
        contract.sign_date = contract_sign_date
        contract.status = contract_status
        contract.project = project_id
        list_contracts.append(contract)
    
    return list_contracts


"""


