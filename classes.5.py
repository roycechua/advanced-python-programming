class Employee:
    interest = 1.05
    def __init__(self, first, last, balance):
        self.first = first
        self.last = last
        self.balance = balance
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    def addInterest(self):
        return float(self.balance)*self.interest 

    @classmethod
    def setInterest(cls, amount):
        # we are working with the clas instead ng instance dito naman ang 
        # kukunin natin ay di na yung self kasi
        # ang gusto na nating iedit ay yung class variable na which is yung interest  
        cls.interest = amount  
    @classmethod
    def from_string(cls, Newemp_str):
        first, last, balance = Newemp_str.split('-')
        return cls(first,last,balance)    

emp_1 = Employee("LLoyd", "Magno", 10000)
emp_2 = Employee("Juan", "dela Cruz", 20000)
Employee.setInterest(2.0)  
print(Employee.fullname(emp_1))   
print("Interest rate:", emp_1.interest)
print("Total with interest: ", Employee.addInterest(emp_1),"\n")
print(Employee.fullname(emp_2))
print("Interest rate:", emp_2.interest)
print("Total with interest:",Employee.addInterest(emp_2),"\n")
emp_3 = Employee.from_string("Choyce-Rua-15000")
print(Employee.fullname(emp_3))   
print("Interest rate:", emp_3.interest)
print("Total with interest: ", Employee.addInterest(emp_3),"\n")