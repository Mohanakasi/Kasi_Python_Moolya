"""print prime numbers from 1 to 20"""
lsit_ = []
def prime_nums(end, start=2):
    global lsit_
    for num in range(start, end+1):
        for i in range(2, num):
            if num %i == 0:
                break
        else:
            lsit_.append(num)
    return lsit_
print(prime_nums(20, 1))


class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_emp_details(self):
        print(self.name, self.id)

obj1 = employee('Mohana kasi', '1098')
obj1.display_emp_details()

string_ = 'Iam Mohana kasi'
print(len(string_))
try:
    print(string_[16])
except IndexError:
    print("index is out of the range")


string_ = 'Iam from moolya'
for index, char in enumerate(string_):
    if index == 5:
        print(char)

