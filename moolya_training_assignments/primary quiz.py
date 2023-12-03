"""1.Write a Python program that takes a string as input and
counts the number of vowels (a, e, i, o, u) in the string"""

string_ = 'This is not predicted'
count_ = 0
for char in string_:
    if char in 'aeiouAEIOU':
        count_ += 1
print(count_)


"""2.Write a Python program that reads the contents of a text file named "sample.txt" 
(assuming it exists in the same directory as the program) and prints the content 
to the console. 
Make sure to handle any potential exceptions that may occur during file handling."""

import os
print(os.getcwd())
with open("sample.txt", 'r') as kasi_sam_file1:
    for line in kasi_sam_file1:
        if line:
            print(line)


"""Write a program that takes two lists as input and 
returns a new list containing common elements found in both lists. 
For example, for input lists [1, 2, 3, 4] and [3, 4, 5, 6], the program should return [3, 4]."""
list1_ = [1,2,3,4]
list2_ = [3,4,5,6]
merge_list = [*list1_, *list2_]
print(merge_list)
new_list = []
for item in merge_list:
    if item not in new_list and merge_list.count(item) > 1:
        new_list.append(item)
print(new_list)

"""Write a program that removes duplicates from a given list while preserving the order of elements. 
For example, [1, 2, 2, 3, 4, 4, 5] should become [1, 2, 3, 4, 5]. Do not convert the list to set."""

list_ = [1,2,2,3,4,4,5]
new_list = []
for item in list_:
    if item not in new_list:
        new_list += [item]
print(new_list)


#Given a square matrix of order n*n, we need to print elements of the matrix in Z form.

"""
Examples:
Input : mat[][] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
Output : 1 2 3 5 7 8 9
Input : mat[][] = {5, 19, 8, 7, 4, 1, 14, 8, 2, 20, 1, 9, 1, 2, 55, 4}
Output: 5 19 8 7 14 20 1 2 55 4
"""


"""Given an input string and a pattern, check if characters in the input string follows the same order 
as determined by characters present in the pattern. Assume there won’t be any duplicate characters in the pattern.
Input:
string = "engineers rock"
pattern = "er";
Output: true
Explanation:
All 'e' in the input string are before all 'r'.
Input:
string = "engineers rock"
pattern = "gsr";
Output: false
Explanation:
There are one 'r' before 's' in the input string."""

# "case 1"

string_ = "engineers rock"
pattern = 'er'
for index, char in enumerate(string_):
    if index>1 and char == 'r':
        temp_ = string_[index: len(string_)-1]
        if 'e' in temp_:
            break
            print('False')
    else:
        continue
else:
    print('True')

string_ = "engineers rock"
pattern = 'gsr'
for index, char in enumerate(string_):
    if index > 1 and char == 'r':
        temp_ = string_[index:len(string_)-1]
        if 's' in temp_:
            print('False')
            break
    else:
        continue
else:
    print('True')



    # string_ = "engineers rock"
    # pattern = 'er'
    # for index, char  in enumerate(string_):
    #     if char == 'r' and index>0:
    #         if string_[index-1] == 'e':
    #             print(char, index, string_[index-1]+char)
    #         else:
    #             print('False')
    #             break
    # else:
    #     print('True')
    #
    # string_ = "engineers rock"
    # pattern = 'er'
    # string_ = "engineers rock"
    # pattern = 'er'
    # for index, char  in enumerate(string_):
    #     if char == 'r' and index>0:
    #         if string_[index-1] == 'e':
    #             print(char, index, string_[index-1]+char)
    #         else:
    #             print('False')
    #             break
    # else:
    #     print('True')



# with open('sample.txt', 'r') as file1:
#     for line in file1:
#         if line.strip():
#             print(line)
#

import csv
with open(r"sample.txt", 'r') as file2:
    # r_obj = csv.reader(file2)
    for row in file2:
        if row.s:
            print(row)