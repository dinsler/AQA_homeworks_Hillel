from lagomorphs import Lagomorphs


class Rabbit(Lagomorphs):
    def __init__(self, habitat: str, diet: str, rabbit_color: str,
                 average_life_expectancy: int, rabbit_name: str):
        super().__init__(habitat=habitat, diet=diet, genus='Rabbits')

        self.__rabbit_color = rabbit_color
        self.__average_life_expectancy = average_life_expectancy
        self.__rabbit_name = rabbit_name

    @property
    def rabbit_color(self) -> str:
        return self.__rabbit_color

    @property
    def average_life_expectancy(self) -> int:
        return self.__average_life_expectancy

    @property
    def rabbit_name(self) -> str:
        return self.__rabbit_name


if __name__ == '__main__':
    bunny = Rabbit(habitat='Australia',
                   diet='grass',
                   rabbit_color='white',
                   average_life_expectancy=5,
                   rabbit_name='Bunny')
    print(bunny.habitat)
    print(bunny.animal_class)
    print(bunny.breeding)
    print(bunny.diet)
    print(bunny.sub_class)
    print(bunny.detachment)
    print(bunny.genus)
    print(bunny.rabbit_color)
    print(bunny.average_life_expectancy)
    print(bunny.rabbit_name)
    print(bunny.get_offspring())
    print(bunny.get_food())
