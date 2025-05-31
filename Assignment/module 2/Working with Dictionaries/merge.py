# #  Write a Python program to merge two lists into one dictionary using a loop.

dict ={}

keys = [1,2,3]
Values = ["a","b","c"]
length = len(keys)

for i in range(length):
   dict[keys[i]]=Values[i]
print(dict)

