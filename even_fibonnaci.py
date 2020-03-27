# This program will return the sum of all even fibonacci numbers  between 0 and  4 million
# this program works!


def next_fib(fib_i, fib_iplus1):
    fib_next = fib_i + fib_iplus1
    return fib_next


f_0 = 1
f_1 = 1

i = 1
sum = 0
while i <= 4000000:
    i = next_fib(f_0, f_1)
    print(i)
    if i % 2 == 0:
        sum += i
    f_0 = f_1
    f_1 = i

print('//')
print(sum)



