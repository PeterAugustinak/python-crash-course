import unittest
from src.chapters.chapter11 import *


class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        result = city_functions("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_functions_population("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile, 500000")


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("John", "Smith", 20000)

    def test_give_default_raise(self):
        self.assertEqual(self.employee.annual_salary, 20000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 30000)


if __name__ == '__main__':
    unittest.main()
