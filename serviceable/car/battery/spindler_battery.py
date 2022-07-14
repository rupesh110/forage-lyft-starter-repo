from abc import ABC
import datetime
from car import Car

class spindlerBattery(Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        
    def needs_service(self, last_service_date):
        service_threshold_date = self.last_service_date.replace(year= self.last_service_date.year()+2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False