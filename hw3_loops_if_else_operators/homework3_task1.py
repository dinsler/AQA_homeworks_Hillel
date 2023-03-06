"""
    Task1. You have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
    The element with an odd index is put into a new list of tuples where the first element
    is the index and the second is the value. [(index, value)]. Accordingly, elements with an even index are
    placed in another list of tuples with the same format as in the case with odd indices.
"""
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_indexes_list = []
odd_indexes_list = []
for index, value in enumerate(my_numbers):
    if index % 2 == 0:
        even_indexes_list.append((index, value))
    else:
        odd_indexes_list.append((index, value))

print(f'List with even indexes is {even_indexes_list}')
print(f'List with odd indexes is {odd_indexes_list}')
