from homework11_all_oop_postulates.interfaces.electric_device_interface import IElectricDevice
from homework11_all_oop_postulates.interfaces.hair_tools_interface import IHairTools


# Inheritance
class HairDryer(IElectricDevice, IHairTools):
    def __init__(self, mode_types: str, styling_nozzles: str):
        self.access_power_source = False
        self.is_on = False
        self.__mode_types = mode_types
        self.__styling_nozzles = styling_nozzles

    @property
    def available_mode_types(self) -> list:
        return ['Cold Air', 'Warm Air', 'Hot Air']

    @property
    def available_styling_nozzles(self) -> list:
        return ['concentrator', 'diffuser']

    def turn_on(self):
        # Encapsulation
        # Abstraction: Function implemented through the abstract class
        self._power_source()
        self.is_on = True
        print('Start drying hair.')

    def turn_off(self):
        # Abstraction: Function implemented through the abstract class
        print('Finish hair drying.')
        self.is_on = False

    def _power_source(self):
        # Abstraction: Function implemented through the abstract class
        print('Hair dryer connected to power source, you can start using.')
        self.access_power_source = True

    def _styling(self, nozzle_name: str):
        # Abstraction: Function implemented through the abstract class
        print(f'Styling with a {nozzle_name}.')
        self.__styling_nozzles = nozzle_name

    def _switch_mode(self, mode_type_name: str):
        # Abstraction: Function implemented through the abstract class
        print(f'{mode_type_name} dry mode selected.')
        self.__mode_types = mode_type_name

    @property
    def mode_type(self) -> str:
        # Hiding
        return self.__mode_types

    @mode_type.setter
    def mode_type(self, mode_type_name: str):
        # Hiding
        if mode_type_name in self.available_mode_types:
            self.__mode_types = mode_type_name
        else:
            raise ValueError(f'Mode type should be from list {self.available_mode_types}')

    @property
    def styling_nozzles(self) -> str:
        # Hiding
        return self.__styling_nozzles

    @styling_nozzles.setter
    def styling_nozzles(self, nozzle_name: str):
        # Hiding
        if nozzle_name in self.available_styling_nozzles:
            self.__styling_nozzles = nozzle_name
        else:
            raise ValueError(f'Styling nozzle should be from list {self.available_styling_nozzles}')

    def operate(self):
        # Encapsulation
        self._styling(nozzle_name='diffuser')
        self._switch_mode('Warm air')
        self.turn_on()
        self.turn_off()
