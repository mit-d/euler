# Factorial digit sum


def Factorial(n):
    for i in range(n, 1, -1):
        n = n * i
    return n


if __name__ == "__main__":
    s = 0
    for i in str(Factorial(100)):
        s = s + int(i)
    print(s)
