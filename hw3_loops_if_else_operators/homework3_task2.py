"""
    Task2.You have the number 2 as a variable.
    Multiply it by 2 in two ways. Accordingly, you need to divide it in 2 different ways by 2.
"""
my_number = 2

multiply_bitwise = bin(my_number << 1)
print(f'Bitwise multiply: {int(multiply_bitwise, 2)}')

multiply = my_number * 2
print(f'Math multiply: {multiply}')

divide_bitwise = bin(my_number >> 1)
print(f'Bitwise divide: {int(divide_bitwise, 2)}')

divide = my_number / 2
print(f'Math divide: {divide}')
