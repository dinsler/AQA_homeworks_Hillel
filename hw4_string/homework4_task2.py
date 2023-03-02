"""
    Task2. There is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"].
    Print to the console the names of each on a new line, right-aligned using the string method and
    formatting via f string. Also, above the names, in the first line, display the headings Names
    where the word names should be in the middle, and the rest of the space is filled with the symbol "*"
"""
my_friends = ["John", "Marta", "James", "Amanda", "Marianna"]
names_header = "Names"
print(names_header.center(20, '*'))
for friend in my_friends:
    print(f'{friend : >20}')
