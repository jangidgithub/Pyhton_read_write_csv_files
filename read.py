# open function ---> use for open any type of file like txt
# read method -----> use for read any file
# tell method -----> use for find cursore posission 
# close method ----> use for close object which we open help of open function
# readline method --> use for read one line 
# seek method ------> use for change cursore position


# f = open("hello.txt")
# print(f"cursore ---> {f.tell()}")
# print(f.read())
# print(f"cursore ---> {f.tell()}")
# print("before seek method")
# f.seek(0)
# print("after seek method")
# print(f"cursore ---> {f.tell()}")
# print(f.read())
# print(f.readline())

f = open(r"D:\python program\read\hello.txt")
for line in f.readlines()[:2]:
    print(line,end='')

f.close()
