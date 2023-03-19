from typing import Union, List
from wagon import Wagon


class Train:
    def __init__(self):
        self.wagons = []
        self.locomotives = []

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        wagon_chain = '-'.join([str(w) for w in self.wagons])
        if self.locomotives:
            return f'<=[HEAD]-{wagon_chain}'
        else:
            return wagon_chain

    def add_wagon(self, wagon: Union[Wagon, List[Wagon]]):
        if isinstance(wagon, list):
            for cab in wagon:
                if cab.is_locomotive:
                    if len(self.locomotives) > 0:
                        raise Exception('Only one locomotive can be present')
                    self.locomotives.append(cab)
                else:
                    self.wagons.append(cab)
        else:
            if wagon.is_locomotive:
                self.locomotives.append(wagon)
            else:
                self.wagons.append(wagon)
