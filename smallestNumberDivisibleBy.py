"""
This is my solution to the fifth problem of The Euler Project
Problem 5: What is the smallest number divisible by every number in the range of 20.


NOT FINISHED YET


"""

from math import sqrt, ceil

"""
The answer to this question has an elegant answer. We begin with the fact that every number is a product of prime 
numbers. Thus, all prime numbers in the range of 2 to n must be multiplied together.

Secondly, we must include the squares/cubes/etc of each prime in the range of 2 to n. This is in case we have 
several multiples of a prime number.
"""

square_primes = []


# This method gets the list of prime numbers in the range of 2 to k
def is_prime(k):
    flag = 0
    for i in range(2, ceil(sqrt(k)) + 1):
        if k % i == 0:
            flag = 1
            break
    if k == 1:
        print('1 is neither prime nor composite')
    else:
        if flag == 0:
            return True
        else:
            return False


# This returns a list of all prime numbers in the range of 2 to k
def prime_numbers(k):
    p = []
    for j in range(2, k):
        if is_prime(j):
            p.append(j)
    return p


# Cleans array - removes primes if their multiples exist in the array
def clean(arr):
    i = 0
    for ele in arr:
        if ele % arr[i] == 0:
            arr.remove(arr[i])
            print(arr)
        i += 1
    return arr


# This is the procedure which gets the powers of primes less than 20.
num_list = prime_numbers(20)
num_list.append(2)

print(num_list)
for number in num_list:
    b = number
    a = b ** 2
    while a <= 20:
        square_primes.append(a)
        a *= b
        num_list.remove(b)
print(square_primes)
print(num_list)

full_factors = num_list + square_primes
# fin_list = clean(full_factors)
p = 1
print(full_factors)
for i in full_factors:
    p *= i
print(p)