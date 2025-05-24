
# f = open("test.txt",'w')
# k = f.write("something about python")
# f.close()

# f=open("test.txt",'r')
# data =f.read()
# print(data)
# f.close()

# f=open("test.txt",'r')
# k = f.readlines()
# print(k)

# while True:
#     data = f.readline()
#     if not data:
#         break
#     if data.startswith('t'):
#         print(data)

# with open("test.txt",'r+') as f:
#     f.seek(15)
#     print(f.tell())
#     data = f.read()
#     print(data)
#     print(f.tell())

    with open("home.txt",'w+') as f:
        f.write("write something")
         f.seek(0)
         data = f.read()
         print(data)
         


