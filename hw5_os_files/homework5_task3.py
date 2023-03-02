"""
    Task3. You have the file text.txt(attached). Please count how many times each letter appears in this file.
"""
import re
import os

if __name__ == '__main__':
    file_path = 'text.txt'
    print(os.path.exists(file_path))

    with open(file_path, 'r') as file:
        file_data = file.read()
        letter_symbols = re.findall(r'[a-zA-Z]', file_data)
        unique_symbols = set(letter_symbols)
        letter_dict = {}

        for letter in unique_symbols:
            letter_dict[letter] = file_data.count(letter)
        sorted_letters = sorted(letter_dict.items())
        print(sorted_letters)
