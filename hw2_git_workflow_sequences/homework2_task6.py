"""
    Task6.You have a group of people with non-unique names.
    Generate a list of non-duplicate names (you cannot use set for this task).
    If there are 2 johns in the list, you need to take only one of them.
    "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
"""
non_unique_names = ['Bob', 'Marley', 'Genna', 'Michael', 'Bob', 'Genna']
unique_names = []
for name in non_unique_names:
    if name not in unique_names:
        unique_names.append(name)
print(unique_names)
