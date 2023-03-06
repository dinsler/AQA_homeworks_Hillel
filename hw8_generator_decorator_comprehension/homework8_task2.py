"""
    Task2.Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
    The solution should work and not freeze your computer.
"""
import sys


def return_square_of_even_numbers():
    counter = 0
    while counter % 2 == 0:
        yield counter ** 2
        counter += 2
        if counter > 1000000000:
            break


if __name__ == '__main__':
    gen = return_square_of_even_numbers()
    print(f'generator size: {sys.getsizeof(gen)}')
    # for even_square in gen:
    #     print(even_square)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
