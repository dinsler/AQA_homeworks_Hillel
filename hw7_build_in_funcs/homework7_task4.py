"""
    Task4.Implement your own implementation of function max and min (* additional argument amount of result,
    if you pass 2, function should return 2 max values from the list)
"""
from typing import Union

points_list = [2, 3, 7, 1, 4, 18, 0]


def custom_max_point(input_list: list, count: int = None) -> Union[list, None]:
    input_list.sort()
    if count:
        if type(count) == int and count < len(input_list):
            return input_list[-count:]
        else:
            print(f"Please enter valid count, count can't be more than {len(input_list) - 1}")
            return None
    return input_list[-1]


def custom_min_point(input_list: list, count: int = None) -> Union[list, None]:
    input_list.sort()
    if count:
        if type(count) == int and count < len(input_list):
            return input_list[:count]
        else:
            print(f"Please enter valid count, count can't be more than {len(input_list)-1}")
            return None
    return input_list[0]


if __name__ == '__main__':
    print(custom_max_point(points_list, 2))
    print(custom_min_point(points_list, 2))
