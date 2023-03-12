from primates import Primates


class Humans(Primates):
    def __init__(self, habitat: str, diet: str, human_race: str,
                 average_life_expectancy: int, human_name: str):
        super().__init__(habitat=habitat, diet=diet, genus='Humans')

        self.__human_race = human_race
        self.__average_life_expectancy = average_life_expectancy
        self.__human_name = human_name

    @property
    def human_race(self) -> str:
        return self.__human_race

    @property
    def average_life_expectancy(self) -> int:
        return self.__average_life_expectancy

    @property
    def human_name(self) -> str:
        return self.__human_name


if __name__ == '__main__':
    marko = Humans(habitat='all over the planet',
                   diet='hamburgers',
                   human_race='negroid',
                   average_life_expectancy=65,
                   human_name='Marko')
    print(marko.habitat)
    print(marko.animal_class)
    print(marko.breeding)
    print(marko.diet)
    print(marko.sub_class)
    print(marko.detachment)
    print(marko.genus)
    print(marko.human_name)
    print(marko.average_life_expectancy)
    print(marko.human_name)
    print(marko.get_offspring())
    print(marko.get_food())
