"""
Task1. Create a class describing any company. For example, Toshiba or Apple
"""


class Company:
    def __init__(self, name: str, country: str, city: str, street: str,
                 charter_capital: int, sphere: str, department: str):
        self.__name = name
        self.__country = country
        self.__city = city
        self.__street = street
        self.__charter_capital = charter_capital
        self.__sphere = sphere
        self.__department = department

    @property
    def available_fields_of_activity(self) -> list:
        """
        Returns: list of available fields of company activity
        """
        return ['medicine', 'finance', 'science',
                'manufacture', 'media', 'technology']

    @property
    def available_names_of_departments(self) -> list:
        """
        Returns: list of available company names of departments
        """
        return ['information systems and technology', 'finance',
                'legal', 'people', 'learning and development', 'global security']

    @property
    def name(self) -> str:
        """
        Returns: Company name
        """
        return self.__name

    @name.setter
    def name(self, company_name: str):
        """
        set valid company name
        """
        if isinstance(company_name, str) and len(company_name) < 20:
            self.__name = company_name.capitalize()
        else:
            raise TypeError('Invalid input, only string with length no more than 20 is supported')

    @property
    def address(self) -> str:
        """
        Returns: company address in format "country, city, street"
        """
        return f'{self.__country}, {self.__city} city, St.: {self.__street}'

    @property
    def country(self) -> str:
        """
        Returns: name of country where company is located
        """
        return self.__country

    @country.setter
    def country(self, country_name: str):
        """
        set valid name of country where company is located
        """
        if isinstance(country_name, str) and len(country_name) < 35:
            self.__country = country_name.capitalize()
        else:
            raise Exception('Invalid input, only string with length no more than 35 is supported')

    @property
    def city(self) -> str:
        """
        Returns: name of city where company is located
        """
        return self.__city

    @city.setter
    def city(self, city_name: str):
        """
        set valid name of city where company is located
        """
        if isinstance(city_name, str) and len(city_name) < 30:
            self.__city = city_name.capitalize()
        else:
            raise TypeError('Invalid input, only string with length no more than 30 is supported')

    @property
    def street(self) -> str:
        """
        Returns: name of street where company is located
        """
        return self.__street

    @street.setter
    def street(self, street_name: str):
        """
        set valid name of street where company is located in format 'name number'
        """
        street_split = street_name.split()
        if len(street_split) != 2:
            raise Exception('Street address should be in format "name number"')

        street_name, building_num = street_split
        if not isinstance(street_name, str) or len(street_name) > 30:
            raise TypeError('Street name should be a string with length no more than 30')
        if not building_num.isdigit() or len(str(building_num)) > 5:
            raise TypeError('Building number should be integer with no more than 5 numbers')
        self.__street = f'{street_name.capitalize()}, {building_num}'

    @property
    def charter_capital(self) -> int:
        """
        Returns: charter capital of company
        """
        return self.__charter_capital

    @charter_capital.setter
    def charter_capital(self, value: int):
        """
        set valid charter capital of company
        """
        if isinstance(value, int) and 5000 < value < 1000000:
            self.__charter_capital = value
        else:
            raise Exception('Charter capital should be integer only, no less than 5000 and no more than 10000000')

    @property
    def sphere(self) -> str:
        """
        Returns: field of company activity
        """
        return self.__sphere

    @sphere.setter
    def sphere(self, field_of_activity: str):
        """
        set valid field of company activity
        """
        if field_of_activity in self.available_fields_of_activity:
            self.__sphere = field_of_activity
        else:
            raise Exception(f'Field of activity should be from list {self.available_fields_of_activity}')

    @property
    def department(self) -> str:
        """
        Returns: company departments
        """
        return self.__department

    @department.setter
    def department(self, department_name: str):
        """
        set valid company department
        """
        if department_name in self.available_names_of_departments:
            self.__department = department_name
        else:
            raise Exception(f'Department name should be from list {self.available_names_of_departments}')

    def increase_charter_capital(self, amount: int) -> int:
        """
        Args:
            amount:
        Returns: charter capital after increasing
        """
        self.__charter_capital += amount
        return self.__charter_capital


if __name__ == '__main__':

    apple = Company(name='Apple', country='Ukraine', city='Odessa', street='Deribasovska 16', charter_capital=300000,
                    sphere='technology', department='global security')
    apple.name = 'Apple'
    print(apple.name)
    apple.country = 'Ukraine'
    apple.city = 'Odessa'
    apple.street = 'deribasovska 156'
    print(apple.address)
    apple.charter_capital = 300000
    print(apple.increase_charter_capital(2000))
    apple.sphere = 'technology'
    print(apple.sphere)
    apple.department = 'global security'
    print(apple.department)
