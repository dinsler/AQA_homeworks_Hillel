"""
Create an iterator that accepts a sequence and can iterate over values in a given range.
CustomIterator(sequence, start_index, end_index)
"""


class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.__current_index = self.start_index

    @staticmethod
    def __validate_index_exists(sequence, val):
        try:
            return sequence[val]
        except IndexError:
            raise IndexError(f'List index: {val} out of range for provided list'
                             f'with a len {len(sequence)}')

    def __setattr__(self, key, val):
        if key == 'start_index':
            sequence = self.__dict__['_CustomIterator__sequence']
            if self.__validate_index_exists(sequence, val):
                if val < 0:
                    # shift index to positive number
                    self.__dict__[key] = len(sequence) + val
                else:
                    self.__dict__[key] = val
        elif key == 'end_index':
            sequence = self.__dict__['_CustomIterator__sequence']
            if self.__validate_index_exists(sequence, val):
                if val < 0:
                    # shift index to positive number
                    val = len(sequence) + val
                if self.__dict__['start_index'] > val:
                    raise SyntaxError('Start index should be less than End index')
            self.__dict__[key] = val
        else:
            self.__dict__[key] = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < self.end_index:
            value = self.__sequence[self.__current_index]
            self.__current_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # slice_cases = [-5, 7]
    # slice_cases = [-3, -8]
    # slice_cases = [-8, -3]
    # slice_cases = [-25, 4]
    # slice_cases = [-5, 40]
    slice_cases = [5, 8]

    print(f"Check for slice {slice_cases}")
    custom = CustomIterator(x, *slice_cases)
    for item in custom:
        print(item)

    print("Check result >>>>>>")
    for p in x[slice_cases[0]:slice_cases[1]]:
        print(p)
