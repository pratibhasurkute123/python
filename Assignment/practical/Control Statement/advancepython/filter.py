#  Write a Python program that filters out even numbers using the filter() function.


len=[1,2,3,4,5,6,7,8]

a=list(filter(lambda num:num%2==0 ,len))
print(a)