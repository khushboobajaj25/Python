#
d ={'x':1}
d1 = {'y':3}
result = filter(lambda s: 0 in s.items(),[d,d1])
print(list(result))
#
# """
# It is better to return result because if we want to add element because we can add in empty and if we write None this will create an exception.
# nums =[1,2,3,4,5,6,7]
# Implementing filter
# def my_filter(func,iter):
#     for item in iter:
#         res = func(item)
#         if res:
#             yield item
#
# even_nos = my_filter(lambda x:x%2==0,nums)
# print(list(even_nos))
# op:[2,54,6]
#
# Implement map:
# def my_map(func,iter):
#         for item in iter:
#             res = fun(item)
#             yield res
# numbers = [1,2,3,4,5,6,7]
# res = map(lambda x:x**2,numbers)
# print(list(res))
# op:[1,4,9,16,25,36,49]
#
# Reduce function:
# def sum(x,y):
#     return x+y
# numbers = [1,2,3,4,5,6,7]
# reduce()-->builtins.py mein nahi hain
# it is located in module function tools so to use reduce func func tool import reduce
# result = reduce(add,nums)
# Implement a reduce:
# """
# """from functools import reduce
# words =["Happy","New","Year"]
# result = reduce(lambda x,y:x+" "+y,words)
# print(result)
# r =[]
# print(bool(r))
# Kwargs?
# def func(param1,**kwargs):
#     print(kwargs)
#
# the type of keyword arguments is dictionary
# func(name="xyz",rollno=5,sem ='iv)
# op:
# dictionary
# If we want to add both args and kwargs
# then we have to first pass args and then kwargs because position,keyword
# """
#
# """"
#
# """
# def mul(x,y):
#     return x*y
#
# def my_reduce (func,iter,initial=None):
#     count =0
#     for val in iter:
#         if count==0 and initial == None:
#             res = val
#             count+=1
#         elif count==0:
#             res = initial
#             count+=1
#             res = func(res,val)
#         else:
#             res =func(res,val)
#
#
#     return res
# #numbers = [2,2,3,4]
# #result = my_reduce(mul, numbers,3)
# #print(result)
#
# def mul(x,y):
#     return x*y
#
#
# # def my_reduce(func,my_iter,initaliser):
# #     length = len(my_iter)
# #     iterable = iter(my_iter)
# #     element = my_iter
# #     while length != 0:
# #         if length == len(my_iter) and initaliser == None:
# #             element = next(iterable)
# #         elif length == len(my_iter) and initaliser:
# #             element = func(next(iterable), initaliser)
# #         else:
# #             element = func(next(iterable), element)
# #         length -= 1
# #     return element
#
#
# def my_reduce(func,my_iter,initialise=None):
#     iterable = iter(my_iter)
#
#     element = my_iter
#     try:
#         if element is  my_iter and initialise:
#             element = initialise
#         element = func(initialise, next(iterable)) if initialise else next(iterable)
#
#         while True:
#             element = func(element,next(iterable))
#     except :
#         pass
#     return element
#
#
# numbers =  {}
# result = my_reduce(mul, numbers, )
# print(result)
# # if initialiser:
# #     x = initialiser
# # else:
# #
# # for i in range(len):
# #
# #     x = func(x,next(iter))
# #
#
# """
#
#
# def my_reduce (add,iter,initial_val):
#
#     res = initial_val
#     for val in iter:
#         res =add(res,val)
#     return  res
#
# result = my_reduce(add, numbers,0)
# print(result)
# """
