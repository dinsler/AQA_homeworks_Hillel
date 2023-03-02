"""
    Task4. You have a file of unknown length. Write a function that will remove all numbers from each line of the file.
"""
import re


def remove_numbers_from_file(file_name: str):
    file_content = open(file_name, "r").read()

    with open(file_name, "w") as file:
        file.write(re.sub(r'\d+', "", file_content))


if __name__ == '__main__':
    remove_numbers_from_file("text_sample.txt")
