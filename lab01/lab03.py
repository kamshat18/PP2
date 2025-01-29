#class task 1
class Stringwork:
    def __init__(self):
        self.text=""
    def getstring(self):
        self.text=input("Ввод строки: ")
    def printstring(self):
        print(self.text.upper())
term =Stringwork()
term.getstring()
term.printstring()

#class task 2

class Shape:
    def __init__(self, length=0): 
        self.length = length

    def area(self):
        return self.length * self.length  

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)  

    def area(self):  
        return f"Area of square = {self.length * self.length}"

shape = Shape() 
square = Square(int(input()))  

print(shape.area())
print(square.area())  

       
