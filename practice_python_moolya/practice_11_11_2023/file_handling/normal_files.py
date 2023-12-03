"""
Opening a file in python:
In python file can be opened in two methods
•	Without context manager
•	With using context manager

Without using context manger:
File_obj  = open(file_name, mode)

With context manager:
with open(file_name, mode) as file_obj:
	pass


Modes:
There are four different methods for opening a file

‘r’   read  opens a file for reading, throws error if file not exist

‘a’   opens a file for appending, creates the file if the file doesn’t exist

‘w’  opens a file for writing, Creates the file if doesn’t exist (overrides the content of the file if already exists)

‘x’   Creates the specified file, returns an error if the file exist


Note: When a file is opened without using context manager (Without with block) file remains open unless we close it manually

	When a file is opened using context manager (using with block) the file remains open unless the control is in the with block. Once the control is outside the with block the file will be automatically closed

file object attributes:
file.closed: returns true if the file is closed
file.mode:  returns access mode with the with the which file is opened
file.name: Returns name of the file
file.readable(): Returns true if the file is opened in read mode
file.writable(): Returns true if the file is opened in write mode
file.close(): closes the file

"""
"""without context manager"""
file_obj = open(r"C:\Kasi_python_moolya\sample_2.txt", 'r')
print(file_obj.mode)
print(file_obj.name)
print(file_obj.readable())
print(file_obj.writable())
print(file_obj.read())
file_obj.seek(0)
print(file_obj.readline())
file_obj.seek(0)
print(file_obj.readlines())
file_obj.seek(0)
for line in file_obj:
    print(line)
file_obj.close()
print(file_obj.closed)



"""with context manager"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file1:
    for line in file1:
        print(line)
        print("***********")
    print(file1.name)
    print(file1.mode)
    print(file1.readable())
    print(file1.writable())
    print(file1.encoding)
    print(file1.closed)
    file1.seek(0)
    print(file1.readlines())
    file1.seek(0)
    print(file1.read())
    file1.seek(0)
print(file1.closed)

"""wap to count the no of lines present in the file"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file2:
    count = 0
    for line in file2:
        if line.strip():
            count += 1
    print(count)

"""wap to print line and line no from the file"""
"""normal method"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file3:
    count = 0
    for line in file3:
        print(count, line)
        count += 1
"""using enumerate"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file4:
    for line_no, line in enumerate(file4):
        print(line_no, line)

"""wap to count the no of words in a given file"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file4:
    count = 0
    for line in file4:
        if line.strip():
            words = line.split()
            count += len(words)
    print(count)

"""wap to print the file from the last oif the file"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file4:
    for line in reversed(list(file4)):
        print(line)

"""wap to count the no of words that are starting with vowels"""
with open(r"C:\Kasi_python_moolya\sample_2.txt", 'r') as file4:
    count_words_vow = 0
    for line in file4:
        if line.strip():
            words = line.split()
            for word in words:
                if word[0].lower() in 'aeiou':
                    count += 1
    print(count)


with open(r"temp23.txt", 'w') as w_file:
    w_file.write('This is Mohana kasi')

with open(r"temp23.txt", 'a') as w_file2:
    w_file2.writelines(['\nits a python world', '\ncontains all objects', '\nhaving intrepretor'])

