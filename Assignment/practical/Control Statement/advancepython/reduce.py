# Write a Python program that uses reduce() to find the product of a list of numbers

from functools import reduce
def mu(res,l):             
    return res*l                           # res means result and l means lenth

l = [1,2,3,4,5]
t = reduce(mu,l)
print(t)