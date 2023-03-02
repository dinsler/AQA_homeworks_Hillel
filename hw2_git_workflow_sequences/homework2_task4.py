"""
    Task4.You have two groups of people. One group consists of omnivores, the other only vegetarians.
    An omnivore is a vegetarian but a vegetarian is not an omnivore.
    Display a list of guests who can eat vegetables and herbs.
"""
omnivores = {'Mark', 'Tony', 'Lucy', 'Jacob'}
vegetarians = {'Phoebe', 'Olaf', 'Monika', 'Ross'}
able_to_eat_vegan_food = vegetarians.union(omnivores)
print(f'List of guests who can eat vegetables and herbs is {list(able_to_eat_vegan_food)}')
