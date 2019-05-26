import math 

# class DecimalToRomanNumeral():
#     order = [1000,500,100,50,10,5,1]
#     # in words
#     def __init__(self,number):
#         self.number = number
#         self.roman = ""
#     # in symbols
#     def convert(self):
#         while(self.number>=1000):
#             self.roman+="M"
#             self.number-=1000
#         while(self.number>=500):
#             self.roman+="D"
#             self.number-=500
#         while(self.number>=100):
#             self.roman+="C"
#             self.number-=100    
#         while(self.number>=50):
#             self.roman+="L"
#             self.number-=50
#         while(self.number>=10):
#             self.roman+="X"
#             self.number-=10
#         while(self.number>=5):
#             self.roman+="V"
#             self.number-=5 
#         while(self.number>=1):
#             self.roman+="I"
#             self.number-=1           

#         return self.roman

class DecimalToRomanNumeral():
    numerals = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    words = {
             0:"",
             1:"One",
             2:"Two",
             3:"Three",
             4:"Four",
             5:"Five",
             6:"Six",
             7:"Seven",
             8:"Eight",
             9:"Nine",
             10:"Ten",
             11:"Eleven",
             12:"Twelve",
             13:"Thirteen",
             14:"Fourteen",
             15:"Fifteen",
             16:"Sixteen",
             17:"Seventeen",
             18:"Eighteen",
             19:"Nineteen",
             20:"Twenty",
             30:"Thirty",
             40:"Forty",
             50:"Fifty",
             60:"Sixty",
             70:"Seventy",
             80:"Eighty",
             90:"Ninety"
            }
    # in words
    def __init__(self,number):
        self.orig_number = number
        self.number = number
        self.roman = ""
        self.thousand_word = ""
        self.hundred_word = ""
    # in symbols
    def convert(self):
        for key, value in (self.numerals).items():
            while(self.number>=key):
                self.roman+=value
                self.number-=key
            
        return self.roman

    def displayInWords(self):
        self.number = self.orig_number
        self.thousands = math.floor(self.number/1000)
        self.hundreds = math.floor((self.number%1000)/100)
        self.tens = math.floor(self.number%100)
        if self.thousands == 0:
            pass
        else:
            self.thousand_word = "thousand"
        if self.hundreds == 0:
            pass
        else:
            self.hundred_word = "-hundred"

        if self.tens<=20 or self.tens in [20,30,40,50,60,70,80,90]: 
            return f"""{self.words[self.thousands]} {self.thousand_word} 
                       {self.words[self.hundreds]}{self.hundred_word} 
                       {self.words[self.tens]}"""
        elif self.tens>20:
            self.tens = math.floor((self.number%100)/10)*10
            self.ones = math.floor(self.number%10)
            return f"""{self.words[self.thousands]} {self.thousand_word} 
                       {self.words[self.hundreds]}{self.hundred_word} 
                       {self.words[self.tens]} {self.words[self.ones]}"""

decimal = int(input("Enter a decimal number: "))
converter = DecimalToRomanNumeral(decimal)
print(converter.convert())
print(converter.displayInWords())