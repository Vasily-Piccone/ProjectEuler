# This program will calculate the largest prime factor of a number
from math import sqrt, ceil


def get_factors(k):
    factors = []
    i = 2
    while k > 1:
        while k % i == 0:
            factors.append(i)
            print(i)
            k /= i
        i += 1
    print(factors)
    return factors


def is_prime(k):
    flag = 0
    for i in range(2, ceil(sqrt(k))):
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


n = 600851475143
f = get_factors(n)

for num in f:
    biggest_prime_factor = 0
    if is_prime(num) is True:
        print(num)
        biggest_prime_factor = num
print(biggest_prime_factor)
