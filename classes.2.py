""" Classes
 - class keyword is used to define a class 
 - class names by convention have their first letter capitalized
 - declaration of class might or might not have a parenthesis User() or User
"""

class User():
    # methods with double underscores are called Dunder Methods like __init__()
    
    def __init__(self, full_name, birthday):
        # The first method self is used to reference the instance example: user1
        # we attach self. to a variable name it is attached to that instance
        # not attaching instance means that it is a global variable and every instance can modify it
        self.name = full_name
        self.birthday = birthday
        # extract first and last name
        name_pcs = full_name.split(" ")
        self.first_name = name_pcs[0]
        self.last_name = name_pcs[1]

user1 = User("Royce Chua","10231997")
print(user1.name)
print(user1.birthday)
print(user1.first_name)
print(user1.last_name)