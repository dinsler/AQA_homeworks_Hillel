"""
Task2. Using the created file in task 1, read the file and perform mathematical operations on each element.
Output the result of the operation to the console.
You cannot use imports to import from the first task module.
"""
import os

if __name__ == '__main__':
    data_path = 'test/data_directory'
    file_name = 'my_list.txt'
    file_path = os.path.join(data_path, file_name)
    math_ops = {'1': '+', '2': '-', '3': '*'}

    with open(file_path, 'r') as file:
        for line in file.readlines():
            left_operand, right_operand, operation = line.strip().split(' ')
            expression = ' '.join((left_operand, math_ops[operation], right_operand))
            print(f'{expression} = {eval(expression)}')
