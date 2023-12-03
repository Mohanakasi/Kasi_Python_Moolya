a = {1,2,'kasi'}
print(len(a))
b  = set(('kasi', 'Mohana', 1090))
print(b)
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.intersection(b))
# a.intersection_update(b)
# print(a)
a = {10, 20, 30, 40, 70}
print(a.pop())
a.remove(40)
a.discard(30)
print(a)


dict_ = {'name': 'kasi', 'place': 'hsr', 'date': 25}
print(dict_['place'])
print(dict_.get('date'))
dict_['place'] = 'bangalore' #override the value of a key
print(dict_)
dict_['age'] = 28
print(dict_)
dict_ = {25: 'age'}
print(dict_)

"for loop"
"while loop"

i = 0
while i<=10:
    if i == 8:
        print("while termintating")
        break
    print(i)
    i += 1
while i<=10:
    if i == 5:
        print("while termintating")
        continue
    print(i)
    i += 1



len()