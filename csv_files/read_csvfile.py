# *********************************************read csv file with reader module 

# from csv import reader


# with open(r"D:\python program\read\data.csv",'r') as file:
#     data = reader(file)
#     # print(data)
#     # print(type(data))
#     next(data)
#     for row in data:
#         print(row)


#*********************************************read csv file with DictReader module 

from csv import DictReader

with open(r"D:\python program\read\data.csv" , 'r') as rt :
    data = DictReader(rt)
    for row in data:
        # print(row)
        print(row['name'])
