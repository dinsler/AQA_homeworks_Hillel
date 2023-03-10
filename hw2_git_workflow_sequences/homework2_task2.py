"""
    Task2.You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
    Show it in code. Keep in mind that people with the same name can be in both companies
"""
eleks_staff = ['Marta', 'Derek', 'Loise', 'Logan', 'Greg']
toshiba_staff = ['Loren', 'Viktor', 'Nancy', 'Greg']
toshiba_staff.extend(eleks_staff)
eleks_staff.clear()
print(f'Toshiba staff list after Eleks takeover is {toshiba_staff}')
print(eleks_staff)
