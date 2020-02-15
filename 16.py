# Power Digit Sum

# 2**15 = 32768, and the sum of the digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of 2**1000?


def SumDigits(n):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans


if __name__ == "__main__":
    print(SumDigits(2 ** 1000))
