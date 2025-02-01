def gramms(ounces): #task1 functions
    return  28.3495231 * ounces
result=gramms(5)
print(result)

#task2 functions
def celcius(f):
    return  (5 / 9) * (f-32)
result = celcius(12)
print(result)

#допустим, у всех по 2 ноги, тогда 35*2=70
#94-70=24
#24/2=12 кроликов
#35-12=23курицы

#task  3 func
def solve(numheads, numlegs):
    kroliki = (numlegs - numheads * 2) // 2
    kurici = numheads - kroliki
    return kroliki, kurici  
result = solve(35, 94)
print(f"Kroliki: {result[0]}, Kurici: {result[1]}")

#task 4 func
def filter_prime(lst):
    primes = []  # Создаем пустой список для простых чисел
    for num in lst:  
        if num > 1:  # Простые числа начинаются с 2
            is_prime = True  
            for i in range(2, int(num ** 0.5) + 1):  # Проверка делителей до sqrt(num)
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)  
    return primes  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print(prime_numbers)  

#task 5 func
from itertools import permutations

def print_permutations(s):
    perm_list = permutations(s)  
    for perm in perm_list:
        print("".join(perm))  
result = input("Vvod stroki: ")
print_permutations(result)

#task 6 func

def rever(s):
    slova = s.split()
    revers= slova[::-1]
    return " ".join(revers)
vvod = input("Vvod stroki:")
result = rever(vvod)
print(result)

#task 7 func 

def has_33(nums):
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3:  
            return True
    return False  
print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))  

#task 8 func 

def spy_game(nums):
    for i in range(len(nums) - 2):  
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:  
            return True
    return False  
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

#task 9 func 

import math
def volume(r):
    return 4/3*math.pi*r**3
result = volume(4)
print (result)

#task 10 func

def uni(list):
    lst = []
    for x in list:
        if x not in lst:
            lst.append(x)
    return lst
print(uni([1, 2, 2, 3, 4, 7, 5]))  
print(uni([1, 1, 1, 1]))  
print(uni([5, 6, 7, 6, 10, 8]))  

#task 11 func

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    revers_s = "".join(reversed(s))
    return s == revers_s
print(is_palindrome("madam"))  
print(is_palindrome("kamshat"))  

#task 12 func

def histogram(lst):
    for number in lst:
        print('*' * number)
histogram([4, 9, 7])

#task 13 func

import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input() 
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()

