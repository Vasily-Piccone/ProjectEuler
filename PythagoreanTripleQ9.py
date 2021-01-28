# What pythagorean triple satisfies a + b + c = 1000? what is the product abc?
from math import sqrt


def pythag_triple(n):
    for b in range(0, n-1):
        for a in range(0, n-1):
            if(sqrt(a**2+b**2)+a+b) == 1000:
                prod = a*b*sqrt(a**2+b**2)
                print(a, b)
                print(prod)
    return prod


def main():
    print(pythag_triple(500))


if __name__ == "__main__":
    main()



