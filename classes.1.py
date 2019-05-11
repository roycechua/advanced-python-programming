""" Classes
 - class keyword is used to define a class 
 - class names by convention have their first letter capitalized
 - declaration of class might or might not have a parenthesis User() or User
"""

class User():
    # methods with double underscores are called Dunder Methods like __init__()
    age = 20 # this is an example of a global variable
    
    def __init__(self, full_name, birthday):
        # The first method self is used to reference the instance example: user1
        # we attach self. to a variable name it is attached to that instance
        # not attaching instance means that it is a global variable and every instance can modify it
        self.name = full_name
        self.birthday = birthday
 
user1 = User("Royce Chua","10231997")
print(user1.name)
print(user1.birthday)
user1.age = 21
print(user1.age)
user2 = User("Chris Mango", "19931205")
print(user2.age)
