from csv import DictReader,DictWriter


# with open(r"D:\python program\read\exercises\lorem.txt" , 'a') as read_file:
#     read_file.seek(150)
#     write_txt = read_file.write(' Rahul Sharma')
    # txt_reader = read_file.read()

    # print(txt_reader)

# *************************************************csv work******************************
 
with open(r"D:\python program\read\exercises\practice.csv" , 'r') as read_file:
    read_csv = DictReader(read_file)
    for lines in read_file:
        print(lines)


