for num in range(1,1001):
count = 0
temp = number

while temp!=0:
    temp//=10
    count+=1

temp = number
sum = 0
while temp !=0:
    rem = temp%10
    sum+= pow(rem,count)
    temp = num//10

if sum == number:
    print("armstrong")
else:
    print("not armstrong")        