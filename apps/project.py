from contract import Contract
import datetime

today = datetime.date.today()

class Project:
    def __init__(self, name, create_date=today, contracts_count=0):
        self.name = name
        self.create_date = create_date
        self.contracts = []
        self.contracts_count = contracts_count

    def __str__(self):
        return f'Project (name={self.name}, date={self.create_date})'


    def add_contract(self, contract):
        if contract.status == 'active' and len(contract) < 1 and contract in self.contracts:
            self.contracts.append(contract)
            contract.project = self
        if contract.status != 'active':
            print('Нельзя добавить неактивный договор к проекту.')
            return
        if contract.status == 'активен' and any(c.status == 'активен' for c in self.contracts):
            print('В проекте уже есть активный договор.')
            return
    
        # Добавляем договор к проекту
        self.contracts.append(contract)
        contract.set_project(self)
        print('Договор добавлен к проекту.')




# bob = Contract('bob')
# bob.status = 1
# print(bob)
# new_project = Project('google')
# new_project.add_contract(bob)
# print(new_project)




# bob = Project('bob')
# print(bob.add_contract('google'))
        
    # def __str__(self):
    #     return f'Project: {self.name}, Created: {self.create_date}, Contracts: {len(self.contracts)}'
