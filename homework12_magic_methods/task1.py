"""
Describe any object of your choice in the class. I want the object to be printed to the console in the following format:
class_name: {
                key: value
}
"""


class Country:
    def __init__(self, country_name):
        self.country_name = country_name

    def __str__(self):
        key = list(self.__dict__.keys())[0]
        value = list(self.__dict__.values())[0]
        return f'{self.__class__.__name__}: {{ \n\t\t\t\t{key}: {value} \n}}'


if __name__ == '__main__':
    ukraine = Country('Ukraine')
    print(ukraine)
