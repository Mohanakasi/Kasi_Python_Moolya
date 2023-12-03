# import json
# temp_ = {'a':100, 'b':1000}
# with open(r"temp.json", 'w') as json_file1:
#     json.dump(temp_, json_file1)
#
# with open(r"temp.json", 'r') as json_file2:
#     dat_dict_ = json.load(json_file2)
#     print(dat_dict_.items())
# import random
#
# list_ = []
#
# print(random.randint(1000,2000))
#     # list_.append(str(random.randint(50, 150)-i + random.randint(100, 200)+i))
#
# # print(list_)
import random

dict_ = {
 "ep_gen_token": "/api-clients/",
  "access_token_body": {
           "clientName": "Postman",
           "clientEmail": "kasimohana{randint(1000,1218)}robo@gmail.com"
        }

}


dict_['access_token_body'].update(clientEmail="newemil")
print(dict_)