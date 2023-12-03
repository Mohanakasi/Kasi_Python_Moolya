"reading from CSV files"
import csv
data_list = []
with open(r"D:\Kasi_learning\my_csv_practice.csv", 'r') as csv_file1:
    r_obj = csv.reader(csv_file1)
    for index, row in enumerate(r_obj):
        print(index, row)

with open(r"D:\Kasi_learning\my_csv_practice.csv", 'r') as csv_file2:
    r_obj = csv.DictReader(csv_file2)
    for row in r_obj:
        for elem in row:
            print(type(row[elem]))




"""write a program to read all the employees in employee table"""
with open(r"D:\Kasi_learning\employees.csv", 'r') as csv_file_emp:
    r_obj = csv.DictReader(csv_file_emp)
    for row in r_obj:
         print(row['FIRST_NAME'],'   ', row['LAST_NAME'])

"""write program to print only the names with salaries > 7000"""
# with open(r"D:\Kasi_learning\employees.csv", 'r') as csv_file_emp:
#     r_obj = csv.DictReader(csv_file_emp)
#     for row in r_obj:
#         if row['SALARY'] > '7000':
#             print(row['FIRST_NAME'], row['SALARY'],'\n')


"""wap to group male and female names""" "(using default dict)"
from collections import defaultdict
dict_ = defaultdict(list)
with open(r'D:\Kasi_learning\employees.csv', 'r') as csv_file5:
    r_obj = csv.DictReader(csv_file5)
    next(r_obj)
    for row in r_obj:
        print(row)
        for key in row:
            if key == 'Gender' and row[key] == 'male':
                dict_['male'] += [row['FIRST_NAME']]
            elif key == 'Gender' and row[key] == 'Female':
                dict_['Female'] += [row['FIRST_NAME']]

    print(dict_)

# dict_ = defaultdict(list)
# with open(r'D:\Kasi_learning\employees.csv', 'r') as csv_file5:
#     r_obj = csv.reader(csv_file5)
#     next(r_obj)
#     for row in r_obj:
#         dict_[row[3]] += [row[1]]
    
# print(dict_)

"writing in csv files"
with open(r'D:\Kasi_learning\employees.csv', 'a') as csv_file5:
    w_obj = csv.DictWriter(csv_file5, ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'Gender', 'EMAIL'])
    w_obj.writerow({'EMPLOYEE_ID': '1008', 'FIRST_NAME': 'Mohana kasi', 'LAST_NAME': 'S', 'Gender': 'Male', 'EMAIL':'kasi.jmr@gmail.com'})
    w_obj.writerows([{'EMPLOYEE_ID': '1009', 'FIRST_NAME': 'Mohana Rao', 'LAST_NAME': 'S', 'Gender': 'Male', 'EMAIL':'kasi@gmail.com'}, {'EMPLOYEE_ID': '1011', 'FIRST_NAME': 'Mohana', 'LAST_NAME': 'S', 'Gender': 'Male', 'EMAIL':'jmr@gmail.com'}, {'EMPLOYEE_ID': '10098', 'FIRST_NAME': 'kasi', 'LAST_NAME': 'S', 'Gender': 'Male', 'EMAIL':'kasi.jmr123@gmail.com'}])


print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
