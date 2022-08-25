# with open(r"D:\python program\read\exer.txt",'r') as rt:
#     with open(r"read\output.txt",'a') as at:
#         for lines in rt.readlines():
#             Name,salary = lines.split(',')
#             at.write(f"{Name}'s salary is {salary}")

# read html file 

with open(r"D:\python program\read\read.html",'r') as webpage:
    with open(r"read\output1.txt",'a') as output:
        for lines in webpage.readlines():
            if '<h1' in lines:
                pos = lines.find('<h1')
                first_quote = lines.find('>',pos)
                second_quote = lines.find('>',first_quote+1)
                url = lines[first_quote+1:second_quote]
                output.write(url)



