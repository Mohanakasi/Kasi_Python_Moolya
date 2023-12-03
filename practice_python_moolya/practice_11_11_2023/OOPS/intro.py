# # # a= 10
# # # class Employee:
# # #     company = "test yanthra"
# # #     global a
# # #     a+=10
# # #     print(a)
# # #     def company_(self):
# # #         return f"company name:{self.company}"
# # #         # print(f"accessing class variable by using instance o/p------>{self.company}")
# # #         # print(f"accessing class variable by using instance o/p------>{employee.company}")
# # #
# # #
# # # "instance creation"
# # # emp1 = Employee()
# # # class temp2:
# # #     print(a)
# # #
# # # obj2 = temp2()
# # #
# # #
# # # class Bird:
# # #     def __init__(self):
# # #         print("iam parent class constr")
# # #
# # #     def intro(self):
# # #         print("There are many types of birds.")
# # #
# # #     def flight(self):
# # #         print("Most of the birds can fly but some cannot.")
# # #
# # #
# # # class sparrow(Bird):
# # #     def flight(self):
# # #         print("Sparrows can fly.")
# # #
# # #
# # # class ostrich(Bird):
# # #     name = 'kasi'
# # #     # def __init__(self):
# # #     #     print("iam child cons")
# # #     #     super().__init__()
# # #     def intro(self):
# # #
# # #         super().__init__()
# # #         print("Ostriches cannot fly.")
# # #
# # #
# # # obj1 = ostrich()
# # # print(hasattr(obj1, 'name'))
# # # setattr(ostrich, "a", 100)
# # # try:
# # #     print(getattr(ostrich, 'ab'))
# # # except AttributeError:
# # #     print("not a correct attribute")
# # #
# # # print(hasattr(ostrich, 'a'))
# # # def greeting(func):
# # #     def wrapper(*args, **kwargs):
# # #         print("Hai")
# # #         return func(*args, **kwargs)
# # #     return wrapper
# # #
# # # @greeting #add = greeting(add)
# # # def add(a, b):
# # #     return a+b
# # #
# # # print(add(10, 20))
# # #
# # #
# # # from temp1 import bike
# # # obj1 = bike()
# # # obj1.mileage()
# # # obj1.engine()
# #
# #
# # class bank_xyz:
# #     ac_num = 1234
# #     ac_bal = 0
# #     _cc_num = 2345
# #     __cc_bal = 0
# #     def display_acc_bal(self):
# #         print(self.ac_num)
# #
# #     def display_cc_details(self):
# #         print(self.__cc_num, self.__cc_bal)
# #
# # obj1 = bank_xyz()
# # print(obj1._cc_num)
# #
# #
#
#
# """abstraction"""
# import time
# from abc import ABC, abstractmethod
# class my_bank(ABC):
#
#     """account data"""
#     ac_hol_name = 'Mohana'
#     _mobile = 8886213059
#     __mpin = 1086
#     __ac_num = 5646
#     __acc_bal = 244
#     __cc_num  = 356
#     __cc_pin = 5677
#     __class_access_pin = 10986
#
#     #making class as abstract
#     @abstractmethod
#     def credit_card_data_fetch(self):
#         pass
#
#     #mpin validation
#     def mpin_validation(self, pin):
#         assert pin == my_bank.__mpin
#
#     #granting autherization pin
#     def grant_auth(self, acc_num, mobile, mpin):
#         assert acc_num == my_bank.__ac_num
#         assert mobile == my_bank._mobile
#         assert mpin == my_bank.__mpin
#         return self.__class_access_pin
#
#     #returning cc_details
#     def get_the_cc_data(self, autherization_pin):
#         assert my_bank.__class_access_pin == autherization_pin
#         return self.__cc_num, self.__cc_pin
#
#
# class user_access(my_bank):
#     #user data creation
#     def __init__(self, acc_num, mobile, mpin):
#         self.acc_num = acc_num
#         self.mobile = mobile
#         self.__mpin = mpin
#         self.mpin_validation(self.__mpin)
#
#
#     #getting autheration pin
#     def credit_card_data_fetch(self):
#         __pin = super().grant_auth(self.acc_num, self.mobile, self.__mpin)
#         return __pin
#
#     #generating cc details
#     def display_credit_card_details(self):
#         print(super().get_the_cc_data(self.credit_card_data_fetch()))
#
#
# # user_transaction1 = user_access(5646, 8886213059, 186)
# # # print(dir(user_transaction1))
# # # print(getattr(user_transaction1, "_my_bank__cc_pin"))
# # # print(user_transaction1.credit_card_data_fetch())
# # user_transaction1.display_credit_card_details()
#
#
#
# """after inheriting the abstract class into child class, if your parent abstract classs
# having private variables, even though after creating of object in child
# using the child object, using dir method you can the attribute name for the
# private variable and using that attribute name you can use getattr() method and get
# the private variable data
#
# to avoide this in parent abstract metod you can create a validation method
# with the argument using assert statment
# and call the same method in the parenyt class in init  after creating argument"""
#
#
# #class decorator
# class wait_deco:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         time.sleep(5)
#         return self.func(*args, **kwargs)
#
#
# @wait_deco # add = wait-deco(add)
# def add(a, b):
#     return a+b
# print(add(18, 66))
#
#
# class temp:
#
#
#     def add(self, a, b=0,c=0):
#         return a+b+c
#
# obj1= temp()
# print(obj1.add(1))
# print(obj1.add(1,24))
# print(obj1.add(1, 2, 3))

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
my_generator = simple_generator()
print(type(my_generator))
# Iterate over the values using a for loop
for value in my_generator:
    print(print(dir(value)))
    print(value)