from predators import Predators


class Panthers(Predators):
    def __init__(self, habitat: str, diet: str, panther_color: str,
                 average_life_expectancy: int, panther_name: str):
        super().__init__(habitat=habitat, diet=diet, genus='Panthers')

        self.__panther_color = panther_color
        self.__average_life_expectancy = average_life_expectancy
        self.__panther_name = panther_name

    @property
    def panther_color(self) -> str:
        return self.__panther_color

    @property
    def average_life_expectancy(self) -> int:
        return self.__average_life_expectancy

    @property
    def panther_name(self) -> str:
        return self.__panther_name


if __name__ == '__main__':
    black_panther = Panthers(habitat='Africa',
                             diet='raw meat',
                             panther_color='black',
                             average_life_expectancy=12,
                             panther_name='Motya')
    print(black_panther.habitat)
    print(black_panther.animal_class)
    print(black_panther.breeding)
    print(black_panther.diet)
    print(black_panther.sub_class)
    print(black_panther.detachment)
    print(black_panther.genus)
    print(black_panther.panther_color)
    print(black_panther.average_life_expectancy)
    print(black_panther.panther_name)
    print(black_panther.get_offspring())
    print(black_panther.get_food())
