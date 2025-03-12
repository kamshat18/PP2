# Write a Python program with builtin function to multiply all the numbers in a list
# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
# Write a Python program that invoke square root function after specific milliseconds.
#TASK1
from functools import reduce
def multiply(s):
    return reduce(lambda x, y: x*y, s)
s = [2,3,4,5]
result = multiply(s)
print(result)


#TASK2
text = " At PP2 course we are learn PYTHON  "
upper_case = len(list(filter(str.isupper, text)))
lower_case = len(list(filter(str.islower, text)))
print(upper_case)
print(lower_case)

#TASK3
def palindrom(s):
    return ''.join(reversed (s))
text = input()
if palindrom(text):
    print(f"{text} is palindrome")
else :
    print(f"{text} is not palindrome")

#TASK4
import time 
import math
def afterr(num, milisec):
    time.sleep(milisec/1000)
    result =math.sqrt(num)
    print(f"Square root of{num}  after {milisec} miliseconds is {result} ")
number= 25100
opozd= 2123
print(afterr(number,opozd))

#TASK5
def all_true(t):
    return all(t)
tuple1 =(True,[1,2,3],'string')
tuple2 =(0,False," ")
print("this elements are ",all_true(tuple1))
print("this elements are ",all_true(tuple2))
 