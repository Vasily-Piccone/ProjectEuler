"""
This is my solution to the 4th problem of The Euler Project.
Problem 4: Find the largest palindrome made by multiplying two 3-digit numbers
"""


def reversed_string(string):
    return string[::-1]


def palindromic(n):
    if str(n) == reversed_string(str(n)):
        return True
    else:
        return False


palindrome = 99099  # This is the largest palindrome I could find by hand. It is the result of 693 X 143
start = 999  # We will loop through 3-digit numbers starting at this one.
p = 999
k = 0

for i in range(100, start):
    for j in range(100, start):
        a = i * j
        if palindromic(a):
            k = a
            print(k)
        if k > palindrome:
            palindrome = k
print(palindrome)
