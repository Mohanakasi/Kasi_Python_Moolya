"when the data is in dynamic in nature we will use regular expressions"
import re
print(re.findall('[Pp]ython', r'This is Python12\n world per the performance of \npython pycharm is perfect'))
# var1= re.search('kasi', 'this is kasi world of imagine') #it will matches the string and return the index where it started
#
# print(var1.start())
# print(var1.end())
#
# print(re.search('[a-zA-z]', 'Mohana kasi'))
# print(re.search('^[a-z]', 'this is mohana123'))
# print(re.search('[a-z]{3}', 'this is kasi')) #maches upto 3 character where it started
#
# print(re.)
# print(re.match('I', 'This is mohana kasi'))
# print(re.match('Iam', 'Iam mohana Kasi'))
# print(re.match('Ka', 'Ka m mohana Kasi'))
print(re.findall(r'\d{2}-\d{2}-\d{4}',r'Hello KASI How are yiu 25-10-2023'))
# print(re.findall())

print(re.findall(r"\(?\)",'This is (secret) world of (pyth) ()'))
print(re.findall('he.*o', 'hello')) #one or many occurances
print(re.findall('he.?o', 'helo')) #0zero or one occurance
print(re.findall('he.{2}o', 'hello'))
print(re.findall('[a-z]', 'hello  hai'))
print(re.findall('[^a-zA-z]', 'hai 12 #$namaste'))
print(re.findall('[^0-9]', 'hai 12 #$namaste'))
print(re.findall('[^a-zA-z0-9]', 'hai 12 #$namaste'))
print(re.findall('\Athe', 'the forest range of the string'))
