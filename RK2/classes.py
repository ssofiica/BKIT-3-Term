# Водитель Автопарк
class Driver:
    def __init__(self, id, fio, pay, id_autopark):
        self.id = id
        self.fio = fio
        self.pay = pay
        self.IdAutopark = id_autopark

class Autopark:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Ap_to_Dr:
    def __init__(self, id_Ap, id_Dr):
        self.id_Ap = id_Ap
        self.id_Dr = id_Dr

Drivers = [
    Driver(1, 'Артаев', 20000, 1),
    Driver(2, 'Алешин', 22000, 2),
    Driver(3, 'Светличко', 20000, 1),
    Driver(4, 'Кунцевский', 25000, 3),
    Driver(5, 'Аверьянов', 26000, 3),
    Driver(6, 'Приходько', 21000, 1)
]

Autoparks = [
    Autopark(1, 'М-Такси'),
    Autopark(2, 'БасЭлитСервис'),
    Autopark(7, 'Авангард'),
    Autopark(3, 'Яндекс-такси'),
    Autopark(12, 'ТК Повозкин')
]

Aps_Drs = [
    Ap_to_Dr(1, 1),
    Ap_to_Dr(2, 2),
    Ap_to_Dr(1, 3),
    Ap_to_Dr(3, 4),
    Ap_to_Dr(3, 5),
    Ap_to_Dr(4, 6),
    Ap_to_Dr(1, 7)
]
