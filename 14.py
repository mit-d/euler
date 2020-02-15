def Collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def ChainSize(n):
    sz = 1
    while n != 1:
        n = Collatz(n)
        sz += 1
    return sz


if __name__ == "__main__":
    chain_size, num = 0, None
    for i in range(1, 1000000):
        sz = ChainSize(i)
        (chain_size, num) = (sz, i) if sz > chain_size else (chain_size, num)
    print("chain size of {} for {}".format(chain_size, num))
