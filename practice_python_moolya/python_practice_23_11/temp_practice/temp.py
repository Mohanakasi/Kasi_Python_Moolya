import csv
with open("C:\Users\USER\Desktop\new_file.csv", 'r') as file2:
    r_obj = csv.reader(file2)
    for row in r_obj:
        if row.strip():
            print(row)