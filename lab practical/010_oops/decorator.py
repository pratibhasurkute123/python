

def add(func):
    def wrapper(*a):
        sum=0
        for i in a:
            sum+=i
            print(f"sum of {a} is {sum}")
    return wrapper

# def mul(fun):
#  def wrapper(*a):
#     mul=0
#     for i in a:
#         mul*=i
#     print(f"mul of {a} is {mul}")
#     return wrapper



@add
def calc(a,b):
    pass
calc(10,20)   
        
        
