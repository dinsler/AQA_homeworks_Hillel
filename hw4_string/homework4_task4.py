"""
Task4.You have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] convert it
 to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
"""
import re
camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for word in camel_case_list:
    words_list = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', word)
    snake_case_str = "_".join(words_list).lower()
    snake_case_list.append(snake_case_str)
print(snake_case_list)
