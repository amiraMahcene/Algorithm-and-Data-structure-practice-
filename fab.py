from typing import Dict
from functools import lru_cache

# this is our first excercice 
# The fabonacci sequence, the fabonacci sequence is a sequence of numbers such that any number expect the first 
# and second, is the sum of the pervious one
# 0,1,2,3,5,8,13....
# the value of the first number in the sequence is 0

def fab(n):
    if n == 0 or n == 1:
        return n
    else:
        return fab(n-2) + fab(n-1)
        

print(fab(5))
print(fab(6))
print(fab(8))
# Now we are going to use the technique of memoization 
# Memoization technique in which you store the results of computational task when they are completed
# so that when you need them again , you can look them up instead of needing to compute them again 




memo :Dict[int, int] = {0:0, 1:1}  # our base case

def fab1(n) :
    if n not in memo:
        memo[n] = fab1(n-1) + fab1(n-2)  # memozation 
        return memo[n]
    else:
        return memo[n]

print(fab1(8))  

# The automatic memozation using the built-in decorator pattern , each  time we call the function with 
# new argument we cached the result 


@lru_cache(maxsize=None) 
def fab2(n):
    if n<2:
        return n
    else:
        return fab2(n-1) + fab2(n-2)
    

print(fab2(8))

# Generate fibanacci number with a generator 
# what we mean by generator in python?? in general too 
# Generator is a function with yield keybord Istead of return
# It support iteration and return generator iterator by calling yiled
# generator can have one or more yiled 
# by using next() it resume from where it called yiled  not from the beginnig 


def mygenerator():
    yield 1
    yield 2 
    yield 3 
    yield 4

mygen = mygenerator()
print (mygen)
print(next(mygen))
print("#" *50)
print(next(mygen))

# let's try for loop to see the iteration

for _ in mygen:
    print(_)
# the out put the last two value 3 and 4, because it resume from the last iteration, it won't get back to the first element of the generator
# Ehuuuuum I liked this generator

# let's understand the point we did not understand yesturday
# okay 
def fab3(n):
    if n == 0 :
        return n
    else:
        last = 0
        next = 1
        for _ in range(1,n):
            last, next = next, last+next
        return next
    
print(fab3(5))
# I got it lemme explain 
# all the secret is here :  The right-hand side (next, last+next) is evaluated first.
# last+next: This calculates the sum of last and next. This is the new value for next.
# next: This is the current value of next. This is the new value for last.
# simultaneous or parallel assignment