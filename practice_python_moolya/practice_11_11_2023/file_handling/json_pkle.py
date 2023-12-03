"""json"""
import json

# Python dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Serialize to JSON (python to json)
json_data = json.dumps(data)
print(json_data)

#save to a file
with open(r"data.json", 'w') as js_file:
    json.dump(data, js_file)

#deserilization (json to python)
with open(r"data.json", 'r') as js_file1:
    ds_data = json.load(js_file1)
    print(type(ds_data))
    for key in ds_data:
        print(key)



"""pickele"""
import pickle
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

#serilizing python object to pickle
pk_data = pickle.dumps(data)
print(pk_data)

#deserialize pickle data to python object
print(pickle.loads(pk_data))

#serializing python data to pickle into a file
with open(r"pk_data1.pkl", 'wb') as pk_file1:
    pickle.dump(data, pk_file1)

#deserializing the pickle data from pkl file
with open(r"pk_data1.pkl", 'rb') as pk_data1:
    print(pickle.load(pk_data1))

