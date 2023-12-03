
# a = open('sample.txt', 'r')
# print(a.read())
# print()

import os
print(os.getcwd())
with open('sample.txt', 'r') as file1:
    for line in file1.readlines():
        if line.strip():
            print(line)


# with open('sample.txt', 'a') as file2:
#     file2.write('\nMohaan')

# with open('sample.txt', 'r') as file3:
#    list_ = file3.readlines()
#    print(list_)
# with open('sample.txt', 'w') as file4:
#     for line in reversed(list_):
#         print(line)
#         file4.write('\n{line}')

# import csv
# with open

#lists
list_ = [1,2,3,4]
print(list_.pop(-1))

import csv
with open(r"C:\Users\USER\Desktop\new_file.csv", 'r') as csv_file1:
    r_obj = csv.DictReader(csv_file1)
    for row in r_obj:
        print(row)
    

import csv
with open(r"C:\Users\USER\Desktop\new_file.csv", 'w') as csv_file1:
    w_obj = csv.DictWriter(csv_file1, ['name', 'loc'])
    w_obj.writeheader()
    w_obj.writerow({'name':'Mohana', 'loc':'gnt'})
    w_obj.writerows([{'name':'kasi', 'loc':'gnt'}, {'name':'Rao', 'loc':'gnt'}])
