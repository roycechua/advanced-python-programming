class Student:
    """ This is a class/template for a student object. """
    passing = 50

    def __init__(self, full_name, gender, grades):
        self.full_name = full_name
        self.gender = gender
        self.grades = grades

    def getGPA(self):
        """ This returns the GPA of the student. """
        self.gpa, self.sum = 0.0,0.0
        for key, value in self.grades.items():
            self.sum+=float(value)
        self.gpa = self.sum/len(self.grades)    
        return self.gpa

    def gradeStatus(self):
        """ This returns a string message indicating whether the student passed or not. """
        # def getSalutation(gender):
        #     if gender=="M": 
        #         return "He" 
        #     elif gender=="F": 
        #         return "She" 
        # if self.getGPA()>=passing:
        #     return f"{getSalutation(self.gender)} passed"
        # else:
        #     return f"{getSalutation(self.gender)} failed"   

        self.pronoun = lambda gender: "He" if gender=="M" else ("She" if gender=="F")
        if self.getGPA()>=self.passing:
            return f"{self.pronoun(self.gender)} passed"
        else:
            return f"{self.pronoun(self.gender)} failed"   

    @classmethod
    def setPassingGrade(cls, new_grade):
        cls.passing = new_grade

s1 = Student("Royce Chua","M",{"Eng":62,"Math":63,"Fil":64,"Sci":68,"History":66})
print(f"{s1.full_name}'s GPA is {s1.getGPA()}")
print(s1.gradeStatus())
print(s1.grades)
print("Changed the passing grade to 70")
Student.setPassingGrade(70)
s2 = Student("Joyce Rua","F",{"Eng":68,"Math":59,"Fil":70,"Sci":65,"History":64})
print(f"{s2.full_name}'s GPA is {s2.getGPA()}")
print(s2.gradeStatus())
print(s2.grades)
s3 = Student("Joshua Jimenez","M",{"Eng":63,"Math":62,"Fil":67,"Sci":64,"History":69})
print(f"{s3.full_name}'s GPA is {s3.getGPA()}")
print(s3.gradeStatus())
print(s3.grades)