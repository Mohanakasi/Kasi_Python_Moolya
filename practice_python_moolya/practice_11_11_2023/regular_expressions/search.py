"""search() will try to search the given pattern in the string and gives the first
occurnace character  and the index found"""
"""syntax: re.search(pattern, string)"""
import re
print(re.search('[a-zA-z]', 'Mohana kasi123').group())

#another way of matching patterns
# pattern = re.compile(r"[0-9]")
# found = pattern.search('Mohana kasi1234')
# print(found.start())
# print(found.group())


print(re.search(r'\d', 'Mohana kasi1234'))
print(re.search('^[aeiou]', 'iam Mohana kasi'))
print(re.search('[aeiou]$', 'THis is Mohana kasi'))
print(re.search('f.', 'I am the trainee from 19832 & (batch.~()').start())
print(re.search('f.', 'I am the trainee from 19832 & (batch.~()').endpos)
print(re.search('He.*o', 'Hello hai'))
print(re.search('.+', 'Settipalli'))
print(re.search('T.?', 'This is Mohana'))
print(re.search('is','This is Mohana'))
res = re.search('he.{2}o', 'hello')
print(res.start())
