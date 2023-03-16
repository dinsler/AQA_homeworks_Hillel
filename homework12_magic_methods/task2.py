"""
Task2. Describe the Train object. The class must contain fields and a method for adding wagons
(it is necessary to add objects, instances of the wagon class).
Describe the class Wagon together with the train.
The Wagon must contain a list of passengers and allow adding passengers.
In the Wagon can be 10 passengers for example. When using the len function on a Wagon,
I want to see the number of passengers. When using len on a train, I want to see a list
of Wagons without a locomotive. Each wagon must have a number.
When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon.
***
Implement a train print from task 2. When you print a train, wagons and a locomotive
should be displayed in the console in the following format:
<=[HEAD]-[1]-[2]-[3]-[4]-[...]-[n]-[n-1]
"""

from train import Train
from wagon import Wagon

if __name__ == '__main__':
    wagon_1 = Wagon(1)
    wagon_2 = Wagon(2)
    wagon_3 = Wagon(3)
    locomotive = Wagon(4, is_locomotive=True)
    wagon_1.add_passenger('Gosha')
    wagon_1.add_passenger(['Tosha', 'Lyosha'])
    print(wagon_1.passengers)
    print(len(wagon_1))
    train = Train()
    train.add_wagon(locomotive)
    print(len(train))
    train.add_wagon([wagon_1, wagon_2, wagon_3])
    print(len(train))
    print(train)
