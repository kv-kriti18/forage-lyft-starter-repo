import unittest
from datetime import datetime

from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        car = SpindlerBattery(today,last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        car = SpindlerBattery(today,last_service_date)
        self.assertFalse(car.needs_service())

class TestNubin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = NubbinBattery(today,last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(today,last_service_date)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()

