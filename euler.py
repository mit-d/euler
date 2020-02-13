def factors(n):
    """
    Returns list of all factors of n
    """
    ls = []
    f = 1
    m = n
    while f <= n:
        m = n
        if m % f == 0:
            ls.append(f)
            m /= f
        f = f + 1
    return ls


def list_primality(n):
    """
    Return a list of booleans representing each number in [1,n]'s primality
    """
    # Sieve of Eratosthenes
    result = [True] * (n + 1)  # List of length n with values set to True
    result[0] = result[1] = False  # 1 and 2 are prime
    for i in range(sqrt(n) + 1):
        if result[i]:  # Only compute if not marked False yet
            for j in range(i * i, len(result), i):
                result[j] = False  # mark all multiples
    return result


def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y
