"""
        Task1. Create variables john_salary and marta_salary of some type (floating point).
        Assign the created variables the values you want.
        Print the values of both variables to the console using the print method.
"""
john_salary = 16.7
harry_salary = 21.2
ron_salary = 14.8
marta_salary = 19.5
frodo_salary = 23.2
sam_salary = 15.6
print(f'John\'s salary is {john_salary} dollars per hour')
print(f'Marta\'s salary is {marta_salary} dollars per hour')

"""
    Task2. Create variables john_age and marta_age of integer type. Assign the created variables the values you want.
    Print the values of both variables to the console using the print method.
"""
john_age = 29
harry_age = 24
ron_age = 25
marta_age = 31
frodo_age = 30
sam_age = 30
print(f'John is {john_age} years old')
print(f'Marta is {marta_age} years old')

"""
    Task3. Create string type variables john_name and marta_name. Assign the created variables the values you want. 
    Print the values of both variables to the console using the print method.
"""
john_name = 'John Kovalski'
harry_name = 'Harry Potter'
ron_name = 'Ron Weasley'
marta_name = 'Marta Greenwood'
frodo_name = 'Frodo Baggins'
sam_name = 'Samwise Gamgee'
print(f'Hello, i\'m {john_name}')
print(f'Hello, i\'m {marta_name}')

"""
    Task4. Create boolean variables john_gender and marta_gender. Let john be false and Marta be true. 
    Print the values of both variables to the console using the print method.
"""
john_gender = False
harry_gender = False
ron_gender = False
marta_gender = True
frodo_gender = False
sam_gender = False
print(john_gender)
print(marta_gender)

"""
    Task5. Create variables john_friends and marta_friends. Assign lists to variables. 
    Each list must contain the names of friends. John has his list of friends and Martha has hers.
    Friends (friend's name) can be the usual strings "James", "Peter", etc.
"""
john_friends = ['Harry', 'Ron']
harry_friends = ['Ron', 'Hermione', 'Albus']
ron_friends = ['Harry', 'Hermione']
marta_friends = ['Frodo', 'Sam']
frodo_friends = ['Sam', 'Gandalf', 'Aragorn']
sam_friends = ['Frodo', 'Pippin', 'Merry']

"""
    Task6. Create a list with people's names, some names should be repeated in it.
    Turn a list of duplicate names into a list of unique names using sets.
"""
duplicated_names = ['Frodo', 'Sam', 'Harry', 'Albus', 'Sam', 'Gandalf', 'Frodo']
unique_names = list(set(duplicated_names))
print(f'Unique names are: {unique_names}')

"""
    Task7. Create 2 tuple variables. The tuple must consist of 2 floating point numbers.
    The first value of the tuple is the latitude where you live, 
    and the second value is the longitude where you live.
"""
my_coordinates = (46.48751977208183, 30.729446411132816)

"""Task8. Create 2 variables john, marta. Variables must be dictionaries with keys: 
full_name, age, salary, gender, friends, coordinates.
"""
john_data = {
    'full_name': john_name,
    'age': john_age,
    'salary': john_salary,
    'gender': john_gender,
    'friends': john_friends,
    'coordinates': my_coordinates
}
for key, value in john_data.items():
    print(f'John\'s key => value is: {key} => {value}')

marta_data = {
    'full_name': marta_name,
    'age': marta_age,
    'salary': marta_salary,
    'gender': marta_gender,
    'friends': marta_friends,
    'coordinates': my_coordinates
}
for key, value in marta_data.items():
    print(f'Marta\'s key => value is: {key} => {value}')

"""
    Task from point 8. Instead of strings in the list of friends,
    there should be the same dictionaries as john and marta. 
    Create 2 friends each for John and Martha. Print John and Martha's fields to the console.
"""
harry_data = {
    'full_name': harry_name,
    'age': harry_age,
    'salary': harry_salary,
    'gender': harry_gender,
    'friends': harry_friends,
    'coordinates': my_coordinates
}

ron_data = {
    'full_name': ron_name,
    'age': ron_age,
    'salary': ron_salary,
    'gender': ron_gender,
    'friends': ron_friends,
    'coordinates': my_coordinates
}

frodo_data = {
    'full_name': frodo_name,
    'age': frodo_age,
    'salary': frodo_salary,
    'gender': frodo_gender,
    'friends': frodo_friends,
    'coordinates': my_coordinates
}

sam_data = {
    'full_name': sam_name,
    'age': sam_age,
    'salary': sam_salary,
    'gender': sam_gender,
    'friends': sam_friends,
    'coordinates': my_coordinates
}

john_data['friends'] = [harry_data, ron_data]
print(john_data)

marta_data['friends'] = [frodo_data, sam_data]
print(marta_data)
