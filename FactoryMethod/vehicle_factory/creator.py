from abc import ABC, abstractmethod


class VehicleFactory(ABC):

    @abstractmethod
    def get_vehicle(self, vehicle_type):
        pass

