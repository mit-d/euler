def compute(n):
    sum = int(0)
    a = int(1)
    b = int(2)
    while a < n:
        a, b = b, a + b
        if a % 2 == 0:
            sum += a
    return sum


if __name__ == "__main__":
    print(compute(int(4000000)))
