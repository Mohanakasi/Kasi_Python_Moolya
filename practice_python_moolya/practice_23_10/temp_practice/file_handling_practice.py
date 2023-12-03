#file reading normal files
import os
# print(os.listdir())
# print(os.getcwd())
# os.chdir(r"D:\Kasi_learning")
# print(os.getcwd())
# os.chdir(r"C:\Demo")
# print(os.getcwd())
# os.mkdir(r"D:\Kasi_learning\file_create") #create a new directory
# os.popen(r"C:\Users\USER\Downloads\Kasi_photo.jpg") #opens a file

#file atributes
# with open(r"C:\Users\USER\Desktop\new_file.csv", 'r') as file1:
#     print(file1.readable())
#     print(file1.writable())
#     print(file1.name)
#     os.popen(r"C:\Users\USER\Desktop\new_file.csv")

# with open('Egypt_hist.txt', 'r') as file2:
#     # print(file2.read(0))
#     # print(file2.read(1))
#     # file2.seek(2)
#     print(file2.readline(5))
#     # print(file2.readline(1))
#     print(file2.tell())
#     file2.seek(0)
#     print(file2.tell())
#     print(file2.readline(1))


# with open('Egypt_hist.txt', 'r') as file1:
#     print(file1.read())
#     file1.seek(0)
#     print(file1.read(15))
   
# with open('Egypt_hist.txt', 'r') as file2:
#     print(file2.readline(100))

# with open(r'Egypt_hist.txt', 'r') as file2:
#     count_ = 0
#     for line in file2:
#         count_ += 1
#     print(count_)

# import os
# print(os.getcwd())
"""wap to print line and line no from the file"""
# import csv
# with open("C:\Users\USER\Desktop\new_file.csv", 'r') as file2:
#     r_obj = csv.reader(file2)
#     for row in r_obj:
#         if row.strip():
#             print(row)
    

#file reading normal files
import os
# print(os.listdir())
# print(os.getcwd())
# os.chdir(r"D:\Kasi_learning")
# print(os.getcwd())
# os.chdir(r"C:\Demo")
# print(os.getcwd())
# os.mkdir(r"D:\Kasi_learning\file_create") #create a new directory
# os.popen(r"C:\Users\USER\Downloads\Kasi_photo.jpg") #opens a file

#file atributes
# with open(r"C:\Users\USER\Desktop\new_file.csv", 'r') as file1:
#     print(file1.readable())
#     print(file1.writable())
#     print(file1.name)
#     os.popen(r"C:\Users\USER\Desktop\new_file.csv")

# with open('Egypt_hist.txt', 'r') as file2:
#     # print(file2.read(0))
#     # print(file2.read(1))
#     # file2.seek(2)
#     print(file2.readline(5))
#     # print(file2.readline(1))
#     print(file2.tell())
#     file2.seek(0)
#     print(file2.tell())
#     print(file2.readline(1))


# with open('Egypt_hist.txt', 'r') as file1:
#     print(file1.read())
#     file1.seek(0)
#     print(file1.read(15))
   
# with open('Egypt_hist.txt', 'r') as file2:
#     print(file2.readline(100))

# with open(r'Egypt_hist.txt', 'r') as file2:
#     count_ = 0
#     for line in file2:
#         count_ += 1
#     print(count_)

# import os
# print(os.getcwd())
"""wap to print line and line no from the file"""
# with open('Egypt_hist.txt', 'r') as file2:
#     count_ = 0
#     for line in file2:
#          count_ += 1
#          print(line, '\n', count_, )

# with open('Egypt_hist.txt', 'r') as file3:
#      for line_no, line in enumerate(file3):
#           print(line_no, line, '\n')

# """wap to count the no of words in a given file"""
# with open('Egypt_hist.txt', 'r') as file4:
#      count_ = 0
#      for line in file4:
#           for word in line.split():
#               count_ += 1
#      print(count_)



# """wap to print the file from the last oif the file"""
# with open('Egypt_hist.txt', 'r') as file5:
#      for line in reversed(file5.readlines()):
#           print(line)

# """wap to count the no of words that are starting with vowels"""
# with open('Egypt_hist.txt', 'r') as file5:
#      for line in file5:
#           count_ += 0 
#           for word in line.split():
#                if word[0] in 'aeiouAEIOU':
#                     count_ += 1
#      print(count_)

# """wapto count the no of spaces in the file"""
# with open('Egypt_hist.txt', 'r') as file5:
#      count_ = 0
#      for line in file5:
#         count_ += line.count(' ')
#      print(count_)

# """wap to word and it's count pair in the given list"""
# dict_ = {}
# with open('Egypt_hist.txt', 'r') as file5:
#      for line in file5:
#           for word in line.split():
#                 if word not in dict_:
#                      dict_[word]  = 1
#                 else:
#                      dict_[word] += 1
#      print(dict_)

# from collections import defaultdict
# dict_ = defaultdict(int)
# with open('Egypt_hist.txt', 'r') as file5:
#      for line in file5:
#           for word in line.split():
#                dict_[word] += 1

#      print(dict_)

# "writing into files"
# with open(r"D:\Kasi_learning\file_create\file_for_pract.txt", 'w') as w_file:
#     for _ in range(4):
#         w_file.write('This is Mohana kasi\n')

# with open(r"D:\Kasi_learning\file_create\file_for_pract.txt", 'w') as w_file:
#     for _ in range(4):
#         w_file.write('This is Mohana kasi\n')

# with open(r"D:\Kasi_learning\file_create\file_for_pract.txt", 'w') as w_file:
#     w_file.write('This is kasi') #write method will accept only strings
#     w_file.writelines(['\nthis is rao', '\nfrom guntur']) #write method will take list of strings




         


