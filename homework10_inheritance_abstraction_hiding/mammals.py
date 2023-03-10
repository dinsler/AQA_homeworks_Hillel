from animals import Animals


class Mammals(Animals):

    def __init__(self, habitat: str, diet: str, sub_class: str):
        super().__init__(habitat=habitat, animal_class='Mammals', breeding='heterosexual mating',
                         diet=diet)
        self.__sub_class = sub_class

    def get_offspring(self) -> str:
        return f'The method of reproduction of mammals is {self.breeding}. '

    def get_food(self) -> str:
        return 'Get food as mammal'

    @property
    def sub_class(self) -> str:
        return self.__sub_class
