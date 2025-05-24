

for number in range(0,101):                # in between 1 to 100 find all prime number
    flag = 0

    for i in range(2,number):
        if number %i ==0:
            flag=1
        break

if flag ==0:
    print(number,"prime")
else:   
    
 print(number,"Not prime")    



# number = 13                                #check number is prime or not
# flag = 0

# for i in range(2,number):
#     if number %i==0:
#         flag = 1
#         break

# if flag ==0:
#     print("Prime")
# else:
#     print("not prime")    