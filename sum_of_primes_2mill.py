from math import log


# Upper limit on the number of primes from 2 to n
def primes_to_n(n):
    return (n/log(n))*(1+1.2762/log(n))

def sieve_of_erathosenes(n):
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


def main():
    pass


if __name__ == "__main__":
    pass

