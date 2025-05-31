# # Write a Python program to create a calculator using functions.

def add(a,b):
    return a +b 

def substract(a,b):
    return a-b 

def mul(a,b):
    return a * b    

def divide(a,b):
    return a / b    


print("Select Option")
print("1.add")
print("2.substract")
print("3.mul")
print("4.divide")

choice = input("Enter choice(1/2/3/4):")

if choice in ('1','2','3','4'):
    try:
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter sec number :"))

    except valueError:
        print("Invalid input")
        

if choice == '1':
    print("Result:",add(num1, num2))
elif choice == '2':
    print("Result:",substract(num1, num2))      
elif choice == '3':
    print("Result:",mul(num1 , num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("invalid") 

