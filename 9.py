# Pythagorean Triplet
# a < b < c AND a**2 + b**2 = c**2
#
# Find a the one triplet that exists for a + b + c = 1000


def IsTriplet(a, b, c):
    if a ** 2 + b ** 2 != c ** 2:
        return False
    if a < b < c:
        return True
    else:
        return False


for b in range(1, 999):
    for a in range(1, b):
        c = 1000 - a - b
        # print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(a+b+c) +
        #         str(IsTriplet(a,b,c)))
        if IsTriplet(a, b, c):
            print(a * b * c)
            exit()
