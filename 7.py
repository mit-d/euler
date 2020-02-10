from math import floor, sqrt

def IsPrime(number):
    biggest = floor(sqrt(number)) + 1
    primap = {}
    for i in range(2, biggest):
        if (number % i) == 0:
            return False
    return True

def NthPrime(number):
    n = 0
    while number >= 0:
        n += 1
        if(IsPrime(n)):
            number -= 1
    return n

if __name__ == '__main__':
    print(NthPrime(10001))
    
