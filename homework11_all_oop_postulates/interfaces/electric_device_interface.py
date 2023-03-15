from abc import ABC, abstractmethod


class IElectricDevice(ABC):

    @abstractmethod
    def turn_on(self): ...

    @abstractmethod
    def turn_off(self): ...

    @abstractmethod
    def _power_source(self): ...
