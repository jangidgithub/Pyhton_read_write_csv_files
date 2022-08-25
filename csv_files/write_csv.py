# from csv import writer

# with open(r'read\csv_files\data_w.csv','w',newline='') as wt:
#     csv_write = writer(wt)
#     # methods --> writerow
#     csv_write.writerow(['name','state'])
#     csv_write.writerow(['Raj','Delhi'])
#     csv_write.writerow(['Dilip','Haryana'])

# method = writerows

# with open(r'read\csv_files\data_w.csv','w',newline='') as wt:
#     csv_writer = writer(wt)
#     csv_writer.writerows([['Name','country'],['Rahul Sharma','India'],['Mohamad shaik','Dubai']])

from csv import DictWriter

# with open(r'read\csv_files\data_w.csv','w',newline='') as wf:
#     data = DictWriter(wf,fieldnames=['fname','lname','age'])
#     data.writeheader()
#     data.writerow({
#         'fname': 'Rahul',
#         'lname' : 'Jangid',
#         'age' : 23
#     })
#     data.writerow({
#         'fname': 'Prem',
#         'lname' : 'Sharma',
#         'age' : 22
#     })

# USE BOTH READ OR WRITE 

from csv import DictReader


with open(r"D:\python program\read\csv_files\data.csv",'r') as rf:
    with open(r'read\csv_files\data_w.csv','w',newline='') as wf:
        data_read = DictReader(rf)
        data_writer = DictWriter(wf,fieldnames=['fname','lname','contact_no'])
        data_writer.writeheader()
        for row in data_read:
            fname, lname, contact_no = row['fname'], row['lname'], row['contact_no']
            data_writer.writerow({
                'fname' : fname,
                "lname" : lname,
                'contact_no' : contact_no
            })
            data_writer.writerow({
                'fname' : "Prem",
                "lname" : 'Jangid',
                'contact_no' : 8769746577
            })
