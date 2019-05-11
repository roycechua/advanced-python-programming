""" Classes
 - class keyword is used to define a class 
 - class names by convention have their first letter capitalized
"""

class User():
    pass # is used to write code that does nothing

user1 = User()
# we can attach data like first_name, last_name
# the naming convention is based on PEP 8
user1.first_name = "Royce"
user1.last_name = "Chua"
user1.age = 21

print(user1.first_name, " ", user1.last_name)
user2 = User()
# user2 instance can have a first_name and might not have other fields
user2.first_name = "Chris"

