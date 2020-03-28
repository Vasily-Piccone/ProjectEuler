"""
Problem 25: How many digits can be found in the 1000th fibonacci term
NOTE THAT THIS PROBLEM IS NOT YET COMPLETED
"""


# n represents the index
def rec_fibonacci(n):
    if n == 0:
        fib = 1
    elif n == 1:
        fib = 1
    else:
        fib = rec_fibonacci(n-1) + rec_fibonacci(n-2)
    return fib


def it_fibonacci(n):
    f_0 = 1
    f_1 = 1
    for i in range(0,n):
        f_2 = f_0 + f_1
        f_0 = f_1
        f_1 = f_2
    return f_2


def sum_in_string(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


def fib_length(a):
    i = 1000    # case that has 210 digits -> used to save steps
    while len(str(a)) < 1000:
        i += 1
        a = it_fibonacci(i)
        print(i)
    return a


g = fib_length(it_fibonacci(1000))
print(g)
# s = sum_in_string(str(g))
# print(s)
print(len(str(g)))

print(len(str(it_fibonacci(4780))))
