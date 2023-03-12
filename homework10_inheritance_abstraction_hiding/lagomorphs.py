from live_birth import LiveBirth


class Lagomorphs(LiveBirth):
    def __init__(self, habitat: str, diet: str, genus: str):
        self.diet = self.validate_diet(diet)
        super().__init__(habitat=habitat, diet=self.diet, detachment='Lagomorphs')

        self.__genus = genus

    @property
    def genus(self) -> str:
        return self.__genus

    def get_food(self) -> str:
        return 'Lagomorphs are runing and jumping to get food'

    @staticmethod
    def validate_diet(diet: str) -> str:
        diet_type = ['grass', 'leafs', 'bark of tree']
        if diet in diet_type:
            return diet
        else:
            raise ValueError(f'Diet type should be from list {diet_type}')
