# Routes

# Moving only right and down, what is the total number of routes through a
# square of arbitrary size?

# Approach:
# We will have exactly n down moves and n right moves.
# so, our answer will be (n choose k) where n = 40 and k = 20

l0 = []


def Factorial(n):
    ans = 1
    while n > 0:
        ans = n * ans
        n = n - 1
    return ans


def PermutationCount(n, k):
    return int(Factorial(n) / Factorial(n - k))


def CombinationCount(n, k):  # n choose k
    return int(PermutationCount(n, k) / Factorial(k))


if __name__ == "__main__":
    n = 20
    print(CombinationCount(2 * n, n))
