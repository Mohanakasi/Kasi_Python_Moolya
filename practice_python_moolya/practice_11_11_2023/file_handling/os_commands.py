"""os commands"""
import os
print(os.getcwd())
print(os.listdir(r"C:\Kasi_python_moolya"))
os.mkdir(r"C:\Kasi_python_moolya\temp_create1")
os.rmdir(r"C:\Kasi_python_moolya\temp_create1")


"""methods related to file"""
"""popopen
popen(filename, mode): Similar to open(), provides a pipe/gateway and access 
to file directory. 
It will works for only file not for directory
"""

os.popen(r"C:\Kasi_python_moolya\sample_2.txt")
# os.rename(r"C:\Kasi_python_moolya\sample.txt", "C:\Kasi_python_moolya\sample_2.txt")

# os.remove(r"C:\Kasi_python_moolya\sample_2.txt") #deletes the file

print(os.path.exists(r"C:\Kasi_python_moolya\sample_2.txt"))
print(os.path.isdir(r"C:\Kasi_python_moolya\sample_2.txt"))
print(os.path.isfile(r"C:\Kasi_python_moolya\sample_2.txt"))

