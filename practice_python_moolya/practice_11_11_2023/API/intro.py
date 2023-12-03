"""get"""
import requests
# request  =  tests.request(r"https://simple-books-api.glitch.me/api-clients/")
import json
import jsonpath
from urllib.parse import urljoin
url = r"https://simple-books-api.glitch.me"
end_point = r"/api-clients/"
class API:
    def authentication(self):
        global url
        global token
        with open(r"token_get_payload.json", 'r') as file1:
            reg_body = file1.read()
            post_body = json.loads(reg_body)
            url_ = urljoin(url, end_point)
            response = requests.post(url_, json=post_body)
            print(type(response))
            print(type(response.text))
        res = json.loads(response.text)
        print(type(res))
        # token = jsonpath.jsonpath(res, 'accessToken')
        # print(token)
        # print(type(token))

#     def getting_the_books(self):
#         end_point = r"/books"
#         url_ = urljoin(url, end_point)
#         response = tests.get(url_)
#         print(response.text)
#
#     def order_a_book(self):
#         global order_id
#         end_point = r"/orders/"
#         with open(r"order_book.json", 'r') as file2:
#             reg_body = file2.read()
#             post_body = json.loads(reg_body)
#             headers = {'Authorization': 'Bearer '+token[0]}
#         url_ = urljoin(url,end_point)
#         resonse = tests.post(url_, json=post_body, headers=headers)
#         print(resonse.text)
#         id = json.loads(resonse.text)
#         order_id = jsonpath.jsonpath(id, 'id')
#         print(order_id)
#
a = API()
a.authentication()
# a.getting_the_books()
# a.order_a_book()