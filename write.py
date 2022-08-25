# w ---> using for write new file
# a ---> using for write continues our lines 
# r+ --> using for both of read and write but it write from starting index so it overlap to all previous wite words so solve this problem we use 'seek method' then we write


# with open(r"D:\python program\read\hello.txt",'r') as a:
#     print(a.read())
#     a.close()

# with open(r"read\detail.txt",'w') as a :
#     a.write("I am Rahul Sharma\nI am a Python Devloper")
#     a.close()

# with open(r"read\detail.txt",'r+') as a :
#     a.seek(len(a.read()))
#     a.write("\nI am Rahul Sharma\nI am a Python Devloper")
#     # print(a.tell())
#     a.close()


with open(r"D:\python program\read\detail.txt",'r') as rt:
    with open(r"D:\python program\read\hello.txt",'w') as wt :
        wt.write(rt.read())



