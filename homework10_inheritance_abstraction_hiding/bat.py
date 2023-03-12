from cheiroptera import Cheiroptera


class Bat(Cheiroptera):
    def __init__(self, habitat: str, diet: str, bat_color: str,
                 average_life_expectancy: int, bat_name: str):
        super().__init__(habitat=habitat, diet=diet, genus='Bat')

        self.__bat_color = bat_color
        self.__average_life_expectancy = average_life_expectancy
        self.__bat_name = bat_name

    @property
    def bat_color(self) -> str:
        return self.__bat_color

    @property
    def average_life_expectancy(self) -> int:
        return self.__average_life_expectancy

    @property
    def bat_name(self) -> str:
        return self.__bat_name


if __name__ == '__main__':
    brus = Bat(habitat='Asia',
               diet='frogs',
               bat_color='brown',
               average_life_expectancy=12,
               bat_name='Brus Wayne')
    print(brus.habitat)
    print(brus.animal_class)
    print(brus.breeding)
    print(brus.diet)
    print(brus.sub_class)
    print(brus.detachment)
    print(brus.genus)
    print(brus.bat_color)
    print(brus.average_life_expectancy)
    print(brus.bat_name)
    print(brus.get_offspring())
    print(brus.get_food())
