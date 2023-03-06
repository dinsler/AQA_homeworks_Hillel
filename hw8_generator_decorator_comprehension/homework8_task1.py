"""
    Task1. Create a decorator that prints to the console the name of the function that was called.
    The function should work as intended. For example, create a pair of functions
    for the arithmetic operations of summation and multiplication.
    When calling these functions, the result of the operation must be returned and the name of the
    function that was called must be displayed in the console with the result. Small hint (__name__)
"""


def print_name_of_func_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Result of {func.__name__} is {func(*args, **kwargs)}')
    return wrapper


@print_name_of_func_decorator
def sum_operation(number1: int, number2: int) -> int:
    res = number1 + number2
    return res


@print_name_of_func_decorator
def multiply_operation(number1: int, number2: int) -> int:
    return number1 * number2


if __name__ == '__main__':
    sum_operation(43, 56)
    multiply_operation(34, 2)
