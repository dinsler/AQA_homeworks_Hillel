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

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index in range(self.start_index, self.end_index + 1):
            value = self.__sequence[self.__current_index]
            self.__current_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    my_iter = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 6)

    for item in my_iter:
        print(item)
