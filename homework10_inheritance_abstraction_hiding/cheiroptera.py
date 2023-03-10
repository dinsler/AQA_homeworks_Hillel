from live_birth import LiveBirth


class Cheiroptera(LiveBirth):
    def __init__(self, habitat: str, diet: str, genus: str):
        self.diet = self.validate_diet(diet)
        super().__init__(habitat=habitat, diet=self.diet, detachment='Cheiroptera')

        self.__genus = genus

    @property
    def genus(self) -> str:
        return self.__genus

    def get_food(self) -> str:
        return 'Cheiropterases are flying and hunting to get food'

    @staticmethod
    def validate_diet(diet: str) -> str:
        diet_type = ['frogs', 'birds', 'lizards']
        if diet in diet_type:
            return diet
        else:
            raise ValueError(f'Diet type should be from list {diet_type}')
