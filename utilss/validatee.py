'''Для проверки дупликатов проектов или контрактов'''
import sqlite3

def check_contract():
    with sqlite3.connect('db/projects_contracts.db') as bd:
        curs = bd.cursor()
        curs.execute('''
            CREATE TABLE IF NOT EXISTS contracts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT,
                sign_date TEXT,
                status TEXT,
                project_id INTEGER)''')
        # curs.execute('''
        #     CREATE TABLE IF NOT EXISTS projects (
        #         id INTEGER PRIMARY KEY,
        #         name TEXT,
        #         creation_date TEXT)''')
        bd.commit()

        curs.execute('SELECT id, name, creation_date FROM contracts')
        rows = curs.fetchall()
        list_contracts = []
        for row in rows:
            project_id, project_name, project_description = row  # (1, 'Project A', 'Description for Project A') its row
            list_contracts.append(row[1])
            # contracts_name.append(row)
        # return f"Project ID: {project_id}, Name: {project_name}, Description: {project_description}"
        return list_contracts

def check_project():
    with sqlite3.connect('db/projects_contracts.db') as bd:
        curs = bd.cursor()
        # curs.execute('''
        #     CREATE TABLE IF NOT EXISTS contracts (
        #         id INTEGER PRIMARY KEY,
        #         name TEXT,
        #         creation_date TEXT,
        #         sign_date TEXT,
        #         status TEXT,
        #         project_id INTEGER)''')
        curs.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                creation_date TEXT)''')
        bd.commit()

        curs.execute('SELECT id, name, creation_date FROM projects')
        rows = curs.fetchall()

        list_projects = []
        for row in rows:
            contract_id, contract_name, project_description = row  # (1, 'Project A', 'Description for Project A') its row
            list_projects.append(row[1])
        return list_projects

print(check_project())