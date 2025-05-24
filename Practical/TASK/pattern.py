            #     *
            #    * *
            #   * * *
            #    * *
            #     *
 
# for i in range(4,0,-1):          # not proper done
#     print(" "*i," *"*(4-i+1))
# for j in range(0,4):
#     print(" "*j," *"*(4-j+1)) 

import math
# import startwith
from functools import reduce



# a=[1,2,3,4,9,11]

# k= filter(lambda num : math.sqrt(num).is_integer(),a)
# print(list(k))

 

# k = filter(lambda name:name.startwith("k"),names)
# print(list(k))
 

# a=[10,20,30,40,50]

# k=reduce(lambda x,y:max(x,y),a)
# print(k)

names=["harsh","kamlesh","pratibha","vishal","vatsal"]
k=filter(lambda name:name.startswith("p"),names)
print(list(k))


