# Practical Example 7: Write a Python program to calculate grades based on percentage using
#if-else ladder.

marks = int(input("Enter the marks :"))

if marks>85 and marks<=100:
    print("A Grade")
elif marks>70 and marks<=85:
    print("B Grade")
elif marks>45 and marks<=70:
    print("C Grade")
elif marks>35 and marks<=45:
    print("D Grade")
elif marks>0 and marks<=35:
    print("Fail")
else :
    print("invalid")                       