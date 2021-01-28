# The sieve of erathosenes is an ancient algorithm for finding prime numbers
# input an integer, and it will shoot out all prime numbers between
# 2 and n. We use the approximation nlog(n) for the nth prime number's
# upper bound.
from math import sqrt, log

def upper_bound_prime(n):
    return n*log(n) +n*(log(log(n))-0.9385)


def sieve_of_erathosenes(n):
    #  Define upper limit
    upper_limit = int(upper_bound_prime(n))
    primes = []
    for i in range(2, upper_limit+1):
        primes.append(i)

    i = 2
    # from 2 to sqrt(number)
    while (i <= int(sqrt(upper_limit))):
        # if i is in list, delete its multiples
        if i in primes:
            # j will give multiples of i,
            # starting from 2*i
            for j in range(i * 2, upper_limit + 1, i):
                if j in primes:
                    # deleting the multiple if found in list
                    primes.remove(j)
        i = i + 1

    return primes[n-1]


def main():
    print(sieve_of_erathosenes(10001))


if __name__ == "__main__":
    main()


