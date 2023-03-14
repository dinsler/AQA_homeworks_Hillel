from abc import ABC, abstractmethod


class IHairTools(ABC):

    @abstractmethod
    def _styling(self, styling_nozzles: str): ...

    @abstractmethod
    def _switch_mode(self, mode_type: str): ...
