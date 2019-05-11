import datetime
import math

class User():
    """ A member of this social media site. Storing their Full Name and Birthday """

    def __init__(self, full_name, birthday):
        # The first method self is used to reference the instance example: user1
        # we attach self. to a variable name it is attached to that instance
        # not attaching instance means that it is a global variable and every instance can modify it
        self.name = full_name
        self.birthday = birthday
    def age(self):
        """Return the age of the user in years"""
        today = datetime.date(2019,5,11)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd)
        age_in_days = (today - dob).days
        age_in_years = math.floor(age_in_days/365)
        return (age_in_years)

user1 = User("Royce Chua","19971023")
print(user1.name)
print(user1.birthday)
print(f"{user1.age()} years old")
help(user1)