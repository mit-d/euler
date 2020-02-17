from euler import factors


def d(n):
    return sum(factors(n)) - n


def amicable(n):
    m = d(n)
    return True if d(m) == n and m != n else False


if __name__ == "__main__":
    ans = 0
    for i in range(10000):
        ans = ans + i if amicable(i) else ans
    print(ans)
