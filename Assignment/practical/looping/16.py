#  Practical Example 4: Print this pattern using nested for loop:

# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()     