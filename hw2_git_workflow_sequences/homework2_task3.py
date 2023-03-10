"""
    Task3.You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
    Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.
"""
casino_blacklist = {'Julia Roberts', 'Morgan Freeman', 'Jack Nicholson', 'Tom Cruise'}
poker_blacklist = {'Meryl Streep', 'Tom Cruise', 'Tom Hanks', 'Kate Winslet'}
alcohol_blacklist = {'Johnny Depp', 'Al Pacino', 'Tom Cruise', 'Will Smith'}
person_non_grata = alcohol_blacklist.intersection(casino_blacklist, poker_blacklist)
print(f'{person_non_grata} is non grata person in all places of entertainment')

# solutions with operands
persons_non_grata = alcohol_blacklist & casino_blacklist & poker_blacklist
print(persons_non_grata)
