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
