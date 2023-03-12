from mammals import Mammals


class LiveBirth(Mammals):

    def __init__(self, habitat: str, diet: str, detachment: str):
        super().__init__(habitat=habitat, diet=diet, sub_class='Live Birth')

        self.__detachment = detachment

    @property
    def detachment(self) -> str:
        return self.__detachment

    def get_offspring(self) -> str:
        x = super().get_offspring()
        return f'{x} Give birth through placenta'


if __name__ == '__main__':
    rabbit = LiveBirth(habitat='forest',
                       diet='herb',
                       detachment='Lagomorphs')
    print(rabbit.get_offspring())
