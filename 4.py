# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_palindrome(n):
    s = str(n)
    l = s[:math.floor(len(s)/2)]
    r = s[math.ceil(len(s)/2):]
    if l == r[::-1]:
        return True
    return False

