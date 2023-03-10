"""
Describe mammals using principles from the lesson. You should implement different fields and methods.
For example: Animals -> mammals -> flying mammals-> Bird -> Eagle
Minimum 3 chains should be implemented
Classes should be in different modules. You should have at least 5 different classes.
"""

from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, habitat: str, animal_class: str, breeding: str, diet: str):
        self.habitat = habitat
        self.animal_class = animal_class
        self.breeding = breeding
        self.__diet = diet

    @abstractmethod
    def get_offspring(self): ...

    @abstractmethod
    def get_food(self): ...
