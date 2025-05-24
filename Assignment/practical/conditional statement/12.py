    # Practical Example 8: Write a Python program to check if a person is eligible to donate blood
    #using a nested if.

age = int(input("Enter Age :"))



if age>=18:
    weight= float(input("Enter weight :"))
    if weight >= 55:
        print("Eligible for donate blood")
    else:
        print("Not Eligible for donate blood")  
else:
    print("Under 18 not eligible")          
