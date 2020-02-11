# Sum Square Difference

# sum of squares 1**2 + ...... + n**2
# squares of sum (1 + ....... + n)**2

# we want (sum of sq - sq of sum)


def SumOfSquares(number):
    ans = 0
    while number > 0:
        ans += number ** 2
        number -= 1
    return ans


def SquareOfSums(number):
    ans = 0
    while number > 0:
        ans += number
        number -= 1
    return ans ** 2


if __name__ == "__main__":
    n = 100
    print(SquareOfSums(n) - SumOfSquares(n))
