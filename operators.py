# # Arithmetic operator:  +,-,*,/,%, **,//
#
# # // is floor division opertor. it removes the number after the decimal  (9//2) : 4
#
#
# # Assignment operator
# # =, +=, -+, ...... same as arithmetic operator
#
# # comparison operator
# # ==, >, <, <=,>=,!=
#
# # logical operator
# # and, or, not
#
# # binary operator
# # print (5&7)
#
# # Special operato
# # Identity: is, is not
# # x=10  print(x is y) false
# # y=20 print(x is z) true
# # z=x  print (x is not y) true
# # membership: in, not on
# x='python'
# # print('p' in data) true
# print('z' not in x)
#


# import csv
#
# print(dir(csv))
# with open('data.csv', 'r') as file:
#     get_data = csv.reader(file)  #it prints in list format
#     # get_data=csv.DictReader(file) #prints in dictionary format i.e key value
#     for user in get_data:
#         print(user)
# # this data is printed from data.csv file tab


import csv

with open('data.csv', 'w', newline='') as files:
    header = ['s.no', 'name', 'age', 'address']
    fs = csv.DictWriter(files, fieldnames=header)
    fs.writeheader()
    fs.writerow({'s.no':1,'name':'ram','age':20,'address':'ktm'})
    fs.writerow({'s.no': 2, 'name': 'sita', 'age': 22, 'address': 'bkt'})
