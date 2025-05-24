a=153
num = a
count = 0
while a !=0:
   a//=10
   count+=1

  temp = num
  sum = 0
while num !=0:
   rem = num%10
   sum +=pow(rem,count)
   num = num//10

if temp == sum:
   print("Armstrong")
else:
   print("Not Armstrong")         
