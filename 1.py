# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below 1000.

all = list(range(0,1000))

a = set()
for i in all[::3]:
    a.add(i)
for i in all[::5]:
    a.add(i)

print(sum(a))
