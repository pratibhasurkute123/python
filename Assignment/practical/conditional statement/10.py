#Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = 13
number= 0

for i in range(2,num):
    if num % i == 0:
    number = 1
        break

if number==1:
     print(num,"is not a prime num")      
else:
     print(num,"is a prime num")      

