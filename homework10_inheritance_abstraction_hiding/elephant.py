from proboscidians import Proboscidians


class Elephant(Proboscidians):
    def __init__(self, habitat: str, diet: str, elephant_color: str,
                 average_life_expectancy: int, elephant_name: str):
        super().__init__(habitat=habitat, diet=diet, genus='Elephant')

        self.__elephant_color = elephant_color
        self.__average_life_expectancy = average_life_expectancy
        self.__elephant_name = elephant_name

    @property
    def elephant_color(self) -> str:
        return self.__elephant_color

    @property
    def average_life_expectancy(self) -> int:
        return self.__average_life_expectancy

    @property
    def elephant_name(self) -> str:
        return self.__elephant_name


if __name__ == '__main__':
    dambo = Elephant(habitat='Africa',
                     diet='leafs',
                     elephant_color='gray',
                     average_life_expectancy=60,
                     elephant_name='Dambo')
    print(dambo.habitat)
    print(dambo.animal_class)
    print(dambo.breeding)
    print(dambo.diet)
    print(dambo.sub_class)
    print(dambo.detachment)
    print(dambo.genus)
    print(dambo.elephant_color)
    print(dambo.average_life_expectancy)
    print(dambo.elephant_name)
    print(dambo.get_offspring())
    print(dambo.get_food())
