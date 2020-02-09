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

if __name__ == '__main__':
    digit_nums = range(1000)[::-1]

x = 999
ans=0
while(x>0):
    y = 999
    # if our answer is larger than x**2, return
    if((ans) > (x*999)):
        print(ans)
        exit()
    while(y>x):
        if is_palindrome(x*y) and (x*y) > ans:
            ans = x*y
        y -= 1
    x -= 1

