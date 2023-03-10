"""
    Task5.You have a group of guests for the VIP box. The seats in the VIP box are all occupied by these guests.
    There is a group of guests in the common room and there are still places in it. Display 2 groups of guests in code.
"""
vip_box_guests = {
    'a1': 'Robert',
    'a2': 'Hanna',
    'a3': 'Monika',
    'b1': 'Albert'
}
common_room_guests = {
    'f1': 'Frank',
    'f2': 'Ginger',
    'e1': None,
    'e2': None
}
print(vip_box_guests)
print(common_room_guests)

# Solution2 vip_box_guests as tuple(immutable data type) and common_room_guests as list(mutable data type)
# vip_box_guests = ('Robert', 'Hanna', 'Monika', 'Albert')
# common_room_guests = ['Bob', 'Frank', 'Eva', 'Ginger']
# print(f'Tuple of VIP box guests is {vip_box_guests}')
# print(f'List of common room guest is {common_room_guests}')
