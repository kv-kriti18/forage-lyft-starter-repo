from abc import ABC

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        return self.current_date - self.last_service_date >= 2
