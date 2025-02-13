#TASK 1
def squares(n):
    for i in range(1, n+1):  
        yield i * i  
gen = squares(3)
print(list(gen)) 

#TASK 2
def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i       
gen = even(int(input()))
print(list(gen))

#TASK 3
def divisible(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i       
gen = divisible(12)
print(list(gen))

#TASK 4
def squares(a,b):
    for i in range(a, b+1):  
        yield i * i  
gen = squares(1,6)
print(list(gen)) 

#TASK 5
def numbers(n):
    for i in range(n,-1,-1):
        yield i
gen = numbers(5)
print(list(gen))





    
