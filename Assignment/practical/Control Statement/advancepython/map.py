# Write a Python program to apply the map() function to square a list of numbers.

def square(i):
    return i*i

l = [20,30,40,50,60]
i=list(map(square,l))
print(i)
    
