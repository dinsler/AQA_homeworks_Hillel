"""
     Task5. Implement your own all function
"""
from typing import Callable


def custom_all(input_list: list) -> bool:
    """
    Function process list of booleans and checks if all of items are True
    Args:
        input_list: list of booleans

    Returns: True or False

    """
    for x in input_list:
        if not x:
            return False
    return True


def custom_all_with_callback(callback: Callable, input_list: list) -> bool:
    """
    Function process list of items against callback with condition and check if all conditions passed
    Args:
        callback: function which check item and return True or False for particular list item
        input_list: list of any items

    Returns: True or False

    """
    for x in input_list:
        if not callback(x):
            return False
    return True


if __name__ == '__main__':

    my_list = [22, 42, 56, 76]
    my_list2 = [True, True, True]
    # condition = lambda x: x % 2 == 0
    # print(custom_all_with_callback(callback=condition, input_list=my_list))

    res = all([x % 2 == 0 for x in my_list])
    print(res)
    res2 = custom_all([x % 2 == 0 for x in my_list])
    # res22 = custom_all([condition(x) for x in my_list])
    print(res2)
    # print(res22)
    res3 = custom_all(my_list2)
    print(res3)
