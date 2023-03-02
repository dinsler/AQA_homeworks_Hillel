"""
    Task3.Implement your own implementation of the function map
"""
from typing import Callable


def custom_map(callback: Callable, input_list: list) -> list:
    """
    Execute callback function against every input_list element
    Args:
        callback: function which return every list item in upper case
        input_list:list of any items

    Returns:list that matches the conditions

    """
    result = [callback(i) for i in input_list]
    return result


if __name__ == '__main__':
    lowercase_names = ['alfred', 'ben', 'william']
    # print(list(map(str.upper, lowercase_names)))
    print(list(custom_map(str.upper, lowercase_names)))
