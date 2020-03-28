"""
This is the solution of the sixth problem of The Euler Project
Problem 6: Find the difference between the  sum of squares of the first 100 natural numbers and the square of the sum.
"""


def sum(k):
    s = k * (k + 1) / 2
    return s


def sum_of_squares(k):
    s_of_s = k * (k + 1) * (2 * k + 1) / 6
    return s_of_s


dif = ((sum(100)) ** 2) - sum_of_squares(100)
print(dif)