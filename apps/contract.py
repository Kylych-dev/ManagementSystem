import datetime

today = datetime.date.today()


class Contract:
    STATUS_DRAFT = 0
    STATUS_ACTIVE = 1
    STATUS_COMPLETED = 2

    STATUS_CHOICES = {
        STATUS_DRAFT: 'Черновик',
        STATUS_ACTIVE: 'Активен',
        STATUS_COMPLETED: 'Завершен',
    }
    def __init__(self, name, create_date=today, status=STATUS_DRAFT):
        self.name = name
        self.create_date = create_date
        self.sign_date = None
        self.status = status
        self.project = None

    def __str__(self):
        status_str = Contract.STATUS_CHOICES.get(self.status, 'Неизвестно')
        return f'Договор: {self.name}, Статус: {status_str}'

    def set_status(self, status):
        if status in Contract.STATUS_CHOICES:
            self.status = status
        else:
            print('Неверный статус.')

    def get_status(self):
        return Contract.STATUS_CHOICES.get(self.status, 'Неизвестно')



# contract1 = Contract('Contract 1')
#
# print(contract1)
#
# contract1.set_status(Contract.STATUS_ACTIVE)
#
# print(contract1)
#
# status = contract1.get_status()
#
# print(status)
#
# contract1.set_status(54)


'''
class Contract:
    statu = {0: 'draft', 1: 'active'}
    def __init__(self, name):
        self.name = name
        self.status = 0
        
    def __str__(self):
        return f"name={self.name}, status={self.status}"
        
        
class Contract:
    STATUS_DRAFT = 0
    STATUS_ACTIVE = 1
    STATUS_COMPLETED = 2
    
    STATUS_CHOICES = {
        STATUS_DRAFT: 'Черновик',
        STATUS_ACTIVE: 'Активен',
        STATUS_COMPLETED: 'Завершен',
    }
    
    def __init__(self, name, status=STATUS_DRAFT):
        self.name = name
        self.status = status
        self.create_date = None
        self.sign_date = None
        self.project = None
    
    def __str__(self):
        status_str = Contract.STATUS_CHOICES.get(self.status, 'Неизвестно')
        return f"Договор: {self.name}, Статус: {status_str}"
    
    def set_status(self, status):
        if status in Contract.STATUS_CHOICES:
            self.status = status
        else:
            print('Неверный статус.')  
    
    def get_status(self):
        return Contract.STATUS_CHOICES.get(self.status, 'Неизвестно')


'''









'''
по умолчанию создается в статусе черновик 

черновик активен завершен

завершить договор

подтвердить договор

'''
