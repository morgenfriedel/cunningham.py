#! /usr/bin/env python3

from sys import argv
from math import sqrt
from itertools import count, islice

# Arguments
min_length = 3
num_cap = 91304653283578934559359 # Wroblewski

if len(argv) == 2 :
    min_length = argv[1]
    min_length = int(min_length) - 1
elif len(argv) == 3 :
    min_length = argv[1]
    min_length = int(min_length) - 1
    num_cap = argv[2]
    num_cap = int(num_cap)

# Prime Function
def isPrime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

# Cunningham Function
def cunninghamFunc(kind) :

    global min_length, num_cap

    origin = 1
    x = 2
    chain = []

    while (origin <= num_cap):

        if kind == 1:
            num = (x * origin) + (x - 1)
            kind_str = '1st : '
        elif kind ==2:
            num = (x * origin) - (x - 1)
            kind_str = '2nd : '
        
        if (isPrime(num)):
            chain.append(num)
            x = x * 2
        else: 
            if (len(chain) >= min_length and isPrime(origin)):
                print(kind_str + str([origin] + chain))

            chain = []
            origin += 1
            x = 2

    return True

cunninghamFunc(1)
cunninghamFunc(2)