import math as m

# Returns largest factor of the number. Can be used to check if prime
def largest_factor(n):
    n = int(n)
    upper_factor = int(m.floor(m.sqrt(n)))

    for i in range(upper_factor)[::-1]:
        if(n % i == 0):
            return i


def largest_prime_factor(n):
    for i in range(1, largest_factor(n))[::-1]:
        if(n % i == 0):
            if(largest_factor(i) == 1):
                return i

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))

