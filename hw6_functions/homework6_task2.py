"""
    Task2.Write a function square that takes 1 argument, the side of the square,
    and returns 3 values (using a tuple): the perimeter of the square, the area of the square,
    and the diagonal of the square.
"""
import math


def find_square_perimeter_area_diagonal(side: int) -> tuple:
    square_perimeter = side * 4
    square_area = side ** 2
    square_diagonal = math.sqrt(2) * side
    return square_perimeter, square_area, square_diagonal


if __name__ == '__main__':
    print(find_square_perimeter_area_diagonal(10))
