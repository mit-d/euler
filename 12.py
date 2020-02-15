from euler import n_divisors
from itertools import count


def Triangular(n):
    return (n * (n + 1)) / 2


if __name__ == "__main__":
    triangl = 0
    for i in count(1):
        triangl += i
        if n_divisors(triangl) > 500:
            print(triangl)
            exit()
