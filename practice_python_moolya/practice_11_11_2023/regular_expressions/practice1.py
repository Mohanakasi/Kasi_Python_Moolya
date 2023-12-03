import re
"matchina a series or a particular characters"
print(re.findall(r"[0-9]", 'This is kasi 19th sector 0 division line'))
"\d equivalent to [0-9]"
print(re.findall(r'\d','This is kasi 19th sector 0 division line'))
print(re.findall(r'[a-z]', 'is This python3$ language1'))
print(re.findall(r'[A-Z]', 'hey Hello HAI'))
print(re.findall(r"\w", 'This is MOHANA _99 cordor #$()')) #matches alphabests, numbers, _
print(re.findall(r"[a-zA-z0-5]", 'Its not the way of 8886213059'))
print(re.findall(r"\W", 'THis is $kasi 99)()')) #matches only special characters
print(re.findall(r"\A[aeiou]", 'is this way to bangalore'))
print(re.findall(r"[etio]", 'india is a nation of prime'))
print(re.findall(r"888", 'this is kasi 8886213059 number'))
"^ inside a starting of the character set"
"nothing but negation"
print(re.findall(r'[^a-zA-Z0-9]', 'this is $way of ~09')) #matches only special characters
print(re.findall(r"[^0-9]", 'this 99sector@')) #matches othethan numbers
print(re.findall(r"&{2}", 'Hello & Mohana &&'))

"[]+"
"gives  you entire sub string matched in between the range given"
print(re.findall(r"[0-9]+", 'hey hai 67 sector'))
print(re.findall(r"[a-z]+", 'Hey hello man23'))


"word boundary"
"transition between non word to word at front & word to non word transition at back side of the substring\n" \
"then it is called as word boundary"

print(re.findall(r"\b\d{6}\b", 'hey man 522003 is your pincode'))
print(re.findall(r"\b\d{2}\b", 'hey it is +23 degree right'))

"finding the letters startwith k"
print(re.findall(r"\bk\w*\b", 'this is kasi kingdom of kingyard'))

"sum of individual numbers in a string using regular expresssions"
total = 0
string_ = 'hey 23 and sector 29 is full'
list_ = re.findall(r'\d', string_)
print(total := sum([int(item) for item in list_]))


"sum of multiple numbers in a string using regular expressions"
total = 0
found_nums = re.findall(r"\d+", 'this is 34th street 99sector')
print(total:=sum([int(item) for item in found_nums]))

"to find total spaces in a string using regular expressions"
total = []
spaces = re.findall(r"\s", 'this is kasi  hectic not yours')
print(total:=len(spaces))

"to count the number of occurences of each non special characters (only alphabets)"
"usinng default dict"
from collections import defaultdict
dict_ = defaultdict(int)
found_chars = re.findall(r"[a-zA-Z]", 'this is is sample23 string$%')
for char in found_chars:
    dict_[char] += 1

print(dict_)

"count the upper case characters in string using regular expressions"
found_ups = re.findall(r"[A-Z]", 'This is NOT proper LOGIC #$7$')
print(len(found_ups))

# "finding valid phone numbers from a list"
l = ['123-4567-890', '888-621-3059']
valid_nums = re.findall(r"\d{3}-\d{3}-\d{4}", str(l))
print(valid_nums)


"finding phone numbers startiwith 8 or 9 followed by 00 ex(800 or 900)"
l_ = ['123-4567-890', '800-621-3059', '901-789-4568','900-745-3214']
match_des = re.findall(r"[89]00-\d{3}-\d{4}", str(l_))
print(match_des)

l_ = ['888-621-3059', '949-129-4540', '989-840-3459']
match = re.findall(r"\d{3}-\d{3}-\d{2}59\b", str(l_))
print(match)



"finding vowel words in a list"
l = ['iam', 'king', 'user']
match = []
for word in l:
    found = re.findall(r"[aeiou]", word)
    if found:
        match += word
print(match)



