"""
    Task3.Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns
    True if it is a prime number, and False otherwise.
"""


def is_prime(number: int) -> bool:
    if number in range(2, 1001):
        for _ in range(2, number):
            if (number % _) == 0:
                return False
        return True


if __name__ == '__main__':
    print(is_prime(11))
