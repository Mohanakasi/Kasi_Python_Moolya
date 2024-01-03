# # class temp4:
# #     name = 'kasi'
# #     @staticmethod
# #     def add(a, b):
# #         print(a+b)
# #
# # obj1 = temp4()
# # obj1.add(10, 20)
# # print(obj1.__dict__)
# # print(dir(obj1))
# # print(temp4.__dict__)
#
#
# # class temp:
# #
# #     def __init__(self, a):
# #         print('inint oinvoked')
# #         self.a = a
# #     def display(self):
# #         print('kais')
# #     def __call__(self):
# #         print('call method oinvoked')
# #
# #
# # a = temp(10)
# # a()
#
# class wait_deco:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(args[0])
#         return self.func(*args, **kwargs)
#
# @wait_deco
# # @wait_deco
# def add(a, b):
#     print(a+b)
#
# add(10, 10)
#
#
#


string_ = 'Mohana kasi'
for index,char in enumerate(string_):
    print(index, char)

