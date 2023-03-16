from typing import Union, List


class Wagon:
    def __init__(self, wagon_number: int, is_locomotive: bool = False):
        self.wagon_number = self.validate_number(wagon_number)
        self.passengers = []
        self.is_locomotive = is_locomotive

    def __len__(self):
        return len(self.passengers)

    def __repr__(self):
        return f'[{self.wagon_number}]'

    @staticmethod
    def validate_number(wagon_num: int) -> int:
        if not isinstance(wagon_num, int) or wagon_num < 0:
            raise ValueError('Wagon number should be a positive integer')
        return wagon_num

    def add_passenger(self, name: Union[str, List[str]]):
        if self.is_locomotive:
            raise ValueError('Locomotive can\'t have passengers')
        if isinstance(name, list) and self.validate_names(name):
            if len(self.passengers) + len(name) > 10:
                raise Exception(f'Wagon already has {len(self.passengers)}, '
                                f'can\'t fit another {len(name)} passengers')
            self.passengers.extend(name)
        elif isinstance(name, str):
            if len(self.passengers) >= 10:
                raise Exception('Wagon is full')
            self.passengers.append(name)
        else:
            raise ValueError('Passengers name should be string')

    @staticmethod
    def validate_names(names: list):
        for name in names:
            if not isinstance(name, str):
                return False
        return names
