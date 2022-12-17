import unittest
from connections import *
from task1 import a_surname_drivers
from task2 import parks_with_min_drivers_pay
from task3 import drivers_sort


class Testing(unittest.TestCase):
    def test_1(self):
        expected_res = [('Артаев', 20000, 'М-Такси'), ('Алешин', 22000, 'БасЭлитСервис'),
                        ('Аверьянов', 26000, 'Яндекс-такси')]
        self.assertEqual(a_surname_drivers(one_to_many), expected_res)

    def test_2(self):
        expected_res = [('М-Такси', 20000), ('БасЭлитСервис', 22000), ('Яндекс-такси', 25000)]
        self.assertEqual(parks_with_min_drivers_pay(one_to_many), expected_res)

    def test_3(self):
        expected_res = [('Аверьянов', 26000, 'Яндекс-такси'), ('Алешин', 22000, 'БасЭлитСервис'),
                        ('Артаев', 20000, 'М-Такси'),
                        ('Кунцевский', 25000, 'Яндекс-такси'),
                        ('Приходько', 21000, 'М-Такси'),
                        ('Светличко', 20000, 'М-Такси')]
        self.assertEqual(drivers_sort(one_to_many), expected_res)
