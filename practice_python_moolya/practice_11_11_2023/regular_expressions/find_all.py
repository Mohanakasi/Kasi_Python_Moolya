"""findall
The findall() function returns a list containing all matches.
"""
"""Example"""
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"sets"
print(re.findall('[a-m]', "The rain in Spain"))
print(re.findall('^Th', 'The rain in Spain'))
print(re.findall('he..o', 'hello planet'))
print(re.findall('i$', 'This is Mohana Kasi'))
print(re.findall('kasi$', 'This is Mohana kasi'))
print(re.findall('he.*o', 'hello hai'))
print(re.findall('Moh.+a', 'Hello Mohana'))
print(re.findall('Moh.?a', 'Hello Mohana')) #gives only one occurance
print(re.findall(r'\d{2}', 'THis is kasi 12 and the 45 and not 987'))
#Return an empty list if no match was found:
print(re.findall('india', 'iam from guntur'))
print(re.findall(r'\A[aeiou]', 'is this Mohana Kasi'))
print(re.findall(r'\A[aeiou]', 'This this Mohana Kasi'))
print(re.findall(r'\A\d', '19 sector Hello kasi'))

pattern = re.compile(r'\Ath')
print(pattern.findall('this is not the correct of way of doing life prospective'))

pattern = re.compile(r"\A\w")
print(pattern.findall('_1 sector kasi'))
print(pattern.findall('99 sector'))
print(pattern.findall('Aeronatical sector'))
print(pattern.findall('$hello hai python'))

r"""\b finds the match at the begining or ending"""
pattern2 = re.compile(r'\bth')
print(pattern2.findall('this is kasi theoritical world of thomas'))
pattern3 = re.compile(r'an\b')
print(pattern3.findall('its an energitic performance by the shami as a moolyan i can enjoy it'))
pattern4 = re.compile(r"\bat|at\b")
print(pattern4.findall('throat not appropriat at the time of attnendance swat'))

r"""\B find the batch anywhere but not starting or ending of the string"""
pattern = re.compile(r'\Bin')
print(pattern.findall('all becmin ai driven upcoming generating proping moduling and integration toing'))
pattern2 = re.compile(r'\B[0-9]')
print(pattern2.findall('this tro23p conv45terminalogy $5po'))
pattern2 = re.compile(r'\B')


r"""\d finds the all matched digits"""
print(re.findall(r'\d', 'its a great 20fullof23 fullof20and 23terminologu'))
print(re.findall(r'\D', 'its a great 20fullof23 fullof20and 23terminologu'))
print(re.findall(r'\d$', 'oh my god full23 is 8th wonde5'))
print(re.findall(r'^\d', '19th sector banned for34 fine on 18'))

print(re.findall(r'\w', 'hello $rambo$_ is 59 is fine?'))
print(re.findall(r'\W', 'hello $rambo$_ is 59 is fine?'))

found_match = re.findall(r'\s', 'today iam not cominng')
print(found_match)
print(len(found_match))

print(re.findall(r'\S', 'Iam the')) #mathces other than white spaces



pattern = re.compile(r'on\Z')
print(pattern.findall('Iam an ocean on afternoon temperory person'))

print(re.findall(r"\B[+]\d{2} \d{3}-\d{3}-\d{4}", 'this is kasi +91 888-621-3059 number'))

print(re.findall(r'\b\w{2}\b','560001 is a 09 country '))
