#Get the first three characters of a string:
string_ = 'This is Mohana'
print(string_[:3])
"Get the last four characters of a string:"
print(string_[-4:])
#Get every second character of a string:
print(string_[::2])
#Get characters from index 2 to 8 (exclusive) with a step of 2
print(string_[2:8:2])
#Reverse a string:
print(string_[::-1])
#Omitting start index (implicitly starts from the beginning):
print(string_[:5])
#Omitting stop index (implicitly goes until the end):
print(string_[1:])
#Get the last three characters except the last one:
print(string_[-4:-1])
"place holders string formatting"
string2 = 'kasi age is %d %s' % (129, 'yes')
print(string2)

"format()"
string2 = 'This is {} which is {} state'.format('Bnagaliore', 3)
print(string2)

"f-strings"
loc = 'Guntur'
string3 = f'This is not a {loc}'
print(string3)


list_ = ['Mohana', 'Kasi']
print(','.join(list_))
print(dir(tuple))
dict_ = {'[1,2]':'kasi'}


print(a:= 100)
print(str(a))

