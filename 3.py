import math as m
def largest_prime_factor(n):
    upper_factor = m.floor(m.sqrt(n)) 
    return upper_factor

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))

