"""
    Task4. Find all the numbers from 1-1000 that have a 3 in them.
"""


if __name__ == '__main__':

    number_3_in_numbers = [number for number in range(1, 1000) if '3' in str(number)]
    print(number_3_in_numbers)
