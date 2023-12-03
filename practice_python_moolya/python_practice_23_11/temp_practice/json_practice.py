import json
string_ = 'This is kasi file'
s_data = json.dumps(string_)
print(type(s_data))

import pickle
string_ = 'This is kasi kkkkkk file'
s_data = pickle.dumps(string_)
print(s_data)

# dict_ = {'name':'Mohana Kasi'}
# with open(r'C:\Demo\Python_practice\pik_practice.pkl', 'wb') as file1:
#     pickle.dump(file1, dict_)


