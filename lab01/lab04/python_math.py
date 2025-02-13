#TASK 1
import math
degree = 15
radians = math.radians(degree)
print(radians)

#TASK 2
import math
def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2
base1 = 5
base2 = 6
height = 5
print(trapezoid_area(base1, base2, height))

#TASK 3
def polygon_area(n,s):
    return (n*s**2)/4*math.tan(math.pi/n)
n = 4
length = 25
print(round(polygon_area(n,length)))

#TASK 4
base= 5
height= 6
print(float(base*height))
