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





