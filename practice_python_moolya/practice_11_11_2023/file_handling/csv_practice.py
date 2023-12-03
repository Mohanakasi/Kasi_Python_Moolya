import csv

"reading in csv"
with open(r"sample_data.csv", 'r') as csv_file1:
    r_obj = csv.reader(csv_file1)
    r_obj.__next__() #skips the header
    for row in r_obj:
        print(row)

with open(r"sample_data.csv", 'r') as  csv_file1:
    r_obj = csv.DictReader(csv_file1)
    for row in r_obj:
        print(row)


"""write a program to read all the employees in employee table"""
with open(r"sample_data.csv", 'r') as csv_file2:
    r_obj = csv.DictReader(csv_file2)
    for row in r_obj:
        print(row['name'])

"""write program to print only the names with salaries > 7000"""
with open(r'employees.csv', 'r') as csv_file1:
    r_obj = csv.DictReader(csv_file1)
    for row in r_obj:
        if int(row['sal']) > 7000:
            print(row['FIRST_NAME'])

"""wap to group male and female names""" "(using default dict)"
from collections import defaultdict
dict_ = defaultdict(list)
with open(r"employees.csv", 'r') as csv_file1:
    r_obj = csv.DictReader(csv_file1)
    for row in r_obj:
        if row['Gender'] == 'Male':
            dict_['male'] += [row['FIRST_NAME']]
        elif row['Gender'] == 'FeMale':
            dict_['female'] += [row['FIRST_NAME']]

print(dict_)

"""writing into csv_files"""
"using writer()"
with open(r"practice_write.csv", 'w') as csv_file1:
    w_obj = csv.writer(csv_file1)
    w_obj.writerow(['name', 'age', 'loc']) #writer row takes only one iterable as input
    w_obj.writerows([('kasi', 26, 'guntur'), ('Mohana', 28, 'guntur')]) #write rows will a collection of iterables

"using Dictwriter()"
with open('practice_write.csv', 'a') as csv_file2:
    w_obj = csv.DictWriter(csv_file2, ['empid', 'loc', 'desig'])
    w_obj.writeheader()
    w_obj.writerow({'empid':1234, 'loc':'guntur', 'desig':'sdet'})
    w_obj.writerows([{'empid':1986, 'loc':'bangalore', 'desig':'qa1'}, {'empid':10990, 'loc':'guntur', 'desig':'DEV'}])


