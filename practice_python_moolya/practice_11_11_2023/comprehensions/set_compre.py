""""""" set comprehension to create a set of squares from 1 to 10"""""""
print(res:={item**2 for item in range(1, 11)})

"""tuple of index and item using enumewrate"""
list_ = ['ksi','jmr',1,2,3]
print(res:={(item, index) for index, item in enumerate(list_)})

"""use set comprehension  to create a set of tuples having item and it's index pair of list using range()"""
list_ = ['ksi','jmr']
print(res:={(list_[index], index) for index in range(len(list_))})

"""use set comprehension  to create a set of tuples having item and it's lenth pair of list using enumerate()"""
list_ = ['ksi','jmr']
print(res:={(item, len(item)) for item in list_})

"""set comprehension to create a set with even items present in a list"""
list_ = [1,2,3,4,80,55,380,4520]
print(res:={item for item in list_ if item %2 == 0})

"""set comprehension to create a set with if the item has even length keep it as its else reverse it"""
list_ = ['kasi', 'jmr','i','iam']
print(res:={item if len(item) %2 == 0 else item[::-1] for item in list_})
