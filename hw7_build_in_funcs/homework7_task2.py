"""
    Task2.Implement your realization of the function filter
"""
from typing import Callable


def custom_filter(callback: Callable, input_list: list) -> list:
    """
    Function process list of items against callback with condition and check if all conditions passed
    Args:
        callback: function which check every list item length and return items that meet the conditions
        input_list: list of any items

    Returns: list that matches the conditions

    """
    result = [i for i in input_list if callback(i)]
    return result


names_list = ["Jeff", "Alex", "Jonathan", "Richelle", "Anna"]
new_list = names_list
row_len = 5


if __name__ == '__main__':
    # print(list(filter(lambda x: len(x) < row_len, new_list)))
    print(list(custom_filter(lambda x: len(x) < row_len, new_list)))
