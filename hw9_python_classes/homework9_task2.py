"""
    Task2. Create a class with a description of the worker. Any worker. employees.
"""
from typing import Union


class Employee:
    def __init__(self, name: str, age: int, gender: str, experience: int, salary: int):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__experience = experience
        self.__salary = salary
        self.__bonus = None

    @staticmethod
    def __validate_name(name: str) -> str:
        """
        Args:
            name:
        Returns: validated employee's name
        """
        if len(name) not in range(2, 11):
            raise Exception('First and last names should be at least '
                            '2 symbols and not more than 10 symbols length')
        return name.strip().capitalize()

    @property
    def name(self) -> str:
        """
        Returns: employee's name
        """
        return self.__name

    @name.setter
    def name(self, employee_name: str):
        """
        set valid employee's name
        """
        if not isinstance(employee_name, str):
            raise TypeError('Invalid input, only string is supported')
        name_split = employee_name.split()
        if len(name_split) == 2:
            first_name = self.__validate_name(name_split[0])
            last_name = self.__validate_name(name_split[1])
        else:
            raise Exception('Employee\'s name should contain first and last name only')
        self.__name = " ".join([first_name, last_name])

    @property
    def available_genders(self) -> list:
        """
        Returns: list of available gender variants
        """
        return ['male', 'female']

    @property
    def gender(self) -> str:
        """
        Returns: employee's gender
        """
        return self.__gender

    @gender.setter
    def gender(self, sex: str):
        """
        set valid employee's gender
        """
        if sex in self.available_genders:
            self.__gender = sex
        else:
            raise Exception(f'Gender should be in {self.available_genders}')

    @property
    def age(self) -> int:
        """
        Returns: employee's age
        """
        return self.__age

    @age.setter
    def age(self, years: int):
        """
        set employee's age in range 18 - 65
        """
        if 18 <= years <= 65:
            self.__age = years
        else:
            raise Exception('Age should be in range 18 - 65')

    @property
    def experience(self) -> int:
        """
        Returns: years of employee's experience
        """
        return self.__experience

    @experience.setter
    def experience(self, experience_years: int):
        """
        set years of employee's experience in range 0 - 46
        """
        if experience_years not in range(0, 46):
            raise Exception('Experience should be in range 0 - 46')
        else:
            self.__experience = experience_years

    @property
    def salary(self) -> Union[int, float]:
        """
        Returns: employee's salary according to his work experience
        """
        if self.__experience < 3:
            return self.__salary
        elif 3 <= self.__experience < 5:
            return self.__salary + (self.__salary * 0.15)
        elif 5 <= self.__experience < 10:
            return self.__salary + (self.__salary * 0.2)
        else:
            return self.__salary + (self.__salary * 0.25)

    @salary.setter
    def salary(self, amount: Union[int, float]):
        """
        set valid employee's salary
        """
        if not isinstance(amount, (int, float)):
            raise TypeError('Expected amount to be integer or float')
        if amount <= 0:
            raise Exception('Salary can\'t be less or equal to 0')
        else:
            self.__salary = amount

    @property
    def bonus(self):
        """
        Returns: employee's bonus
        """
        return self.__bonus

    @bonus.setter
    def bonus(self, amount: Union[int, float]):
        """
        set employee's bonus
        """
        if not isinstance(amount, (int, float)):
            raise TypeError('Expected amount to be integer or float')
        if amount <= 0:
            raise Exception('Bonus can\'t be less or equal to 0')
        else:
            self.__bonus = amount

    def calculate_salary_with_bonus(self) -> int:
        """
        Returns: employee's salary including bonus
        """
        return self.salary + self.__bonus


if __name__ == '__main__':
    mark = Employee(name='Mark', age=22, gender='male', experience=4, salary=6700)
    mark.name = 'Mark johnson'
    print(mark.name)
    mark.age = 22
    print(mark.age)
    mark.gender = 'male'
    print(mark.gender)
    mark.experience = 5
    print(mark.experience)
    mark.salary = 6700
    print(mark.salary)
    mark.bonus = 500
    print(mark.calculate_salary_with_bonus())
