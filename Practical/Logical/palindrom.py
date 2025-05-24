
 
# for i in range(5,0,-1):
#     for j in range(0,i):
#        print("*",end="")
#     print()


# for i in range(0,5):
#     for j in range(0,i):
#         print(" *",end="")
#     print()

# lines = 10
# for i in range(lines,0,-1):
#     print(" "*i,"*"*((lines-i)*2+1))


    *
   * *
  * * *  // task
   * *
    * 

lines = 5
for i in range(lines,0,-1):
    print(" "*i,"*"*(lines-1)*2+1)
