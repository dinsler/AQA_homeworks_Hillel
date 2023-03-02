"""
    Task1. Implement your own print function. It should work on all operating systems.
    You can't use build-in print function
"""
import sys


def my_print_func(text: str):
    return sys.stdout.write(text)


if __name__ == '__main__':
    my_print_func('Hello World!')
