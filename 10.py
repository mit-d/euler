# sum of all primes under 2000000
# strategy: mark table for every multiple from 1 to sqrt(2000000)

from euler import list_primes

if __name__ == "__main__":
    x = 0
    for i in list_primes(2000000):
        x += i
    print(x)
