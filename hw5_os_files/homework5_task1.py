"""
    Task1. Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
    a. element is an integer that will be the left operand of the expression
    b. element is an integer that will be the right operand of the expression
    c. element is an integer from 1 to 3 where:
    identifies the addition operation
    identifies the subtraction operation
    identifies the multiplication operation
    d. You can put data into a text file with the text form or use the pickle module in binary form.
    If placed as text then each line should contain only elements of one tuple separated by spaces (eg "100 2 3").
    The file must be created by a script in a pre-created \test/data directory tree.
    The directory tree must be created by the script.
    Push only the code to the repository (not directories or file).
"""
import random
import os

my_list = []

if __name__ == '__main__':
    for _ in range(100):
        my_list.append((random.randint(0, 100), random.randint(0, 100), random.randint(1, 3)))
    print(my_list)
data_path = 'test/data_directory'
file_name = 'my_list.txt'
file_path = os.path.join(data_path, file_name)
with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f'{item[0]} {item[1]} {item[2]}\n')
