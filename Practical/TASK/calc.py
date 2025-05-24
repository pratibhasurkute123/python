a=float(input("Enter the first Number:"))
b=float(input("Enter the second Number:"))
Choice = input("Enter Your Choice")
print("select Choice")
print("1. Addition")
print("2. Division")
print("3. Multipication")
print("4. Substraction")

if Choice == '1':
    result=a+b
    print("Addition",result)
elif Choice == '2':
    result=a/b
    print("Division",result)
elif Choice == '3':
    result=a*b
    result("Multipication",result)
elif Choice == '4':
    result=a-b   
    print("Substraction",result)
else:
    print("invalid choice")

    
