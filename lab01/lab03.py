#CLASS TASK 1
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

#CLASS TASK 2

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
       
#CLASS TASK 3

class Shape:
    def __init__(self ,lenght=0):
        self.lenght=lenght    
    def area(self):
        return self.lenght*self.lenght
class Rectangle(Shape):
    def __init__(self, lenght,width):
        self.width = width
        return super().__init__(lenght)
    def area(self): 
        return f"Area of triangle = {self.lenght*self.width}"
shape = Shape() 
triangle = Rectangle(5,7)
print(shape.area())
print(triangle.area())
 
#CLASS TASK 4
import math
class Point:
    def __init__(self,x,y):  
        self.x= x
        self.y=y
    def show(self):
         return f"Point({self.x}, {self.y})"
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
    def dist(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
p = Point(3, 4)   
print(p.show())   

p.move(2, -1)     
print(p.show()) 

distance = p.dist(7, 4)
print(f"Расстояние до точки (7,4): {distance:}")  

#CLASS TASK 5
class Bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Popolnen na {amount}")
            
        else:
            print("Ne dobavleno,vnesite cash")
    def withdrawal(self ,amount): 
        if amount>self.balance :
             print("Nehvatka sredstv")
            
        elif amount> self.balance:
            self.balance-=amount
            print(f"Spisalos': {amount}")
           
    def dostup(self,balance):
        print(f"Dostupno:{self.balance}")

acc = Bank("Kamshat", 1200)
print(acc)
acc.deposit(0)
acc.withdrawal(1600)
acc.dostup("")
print(acc)

#CLASS TASK 6

class Check:
    def __init__(self , num):

        self.num=num
    def is_prime(self):

        if self.num > 1:
            for i in range(2, (self.num//2)+1):
                if (self.num % i) == 0:
                    print(self.num, "is not a prime number")
                    return
                
        print(self.num, "is a prime number")
number = Check(2)  
number.is_prime()

number2 = Check(15)
number2.is_prime()

number3 = Check(17)
number3.is_prime()



 
    
    
    


