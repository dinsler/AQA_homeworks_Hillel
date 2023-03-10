from live_birth import LiveBirth


class Predators(LiveBirth):
    def __init__(self, habitat: str, diet: str, genus: str):
        self.diet = self.validate_diet(diet)
        super().__init__(habitat=habitat, diet=self.diet, detachment='Predators')

        self.__genus = genus

    @property
    def genus(self) -> str:
        return self.__genus

    def get_food(self) -> str:
        return 'Predators are hunting to get food'

    @staticmethod
    def validate_diet(diet: str) -> str:
        diet_type = ['raw meat', 'carrion', 'insects']
        if diet in diet_type:
            return diet
        else:
            raise ValueError(f'Diet type should be from list {diet_type}')


if __name__ == '__main__':
    lion = Predators(habitat='jungle',
                     diet='raw meat',
                     genus='lion')
