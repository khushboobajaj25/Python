# # # Constructor:
# #
# #
# #
# #
# # class Sample:
# #     def __call__(self, *args, **kwargs):
# #         obj = self.__new__()
# #         self.__init__(obj)
# #         return obj
# #     def __new__(cls, *args, **kwargs):
# #         print("I am creating that obj")
# #         return super(Sample, cls).__new__(cls)
# #     def __init__(self):
# #         print(" I am good")
# #
# #
# #
# # s = Sample()
# # print(s)
# # print(type(s))
# # # suppose we have memeber variables as name and age and we also write s.coolege it works to stop that we block
# # # set attribute is the function which we ca
# # #
# # # # self is a veriable name
# #
# #
# # class Integer:
# #
#
# def based_on_parameters(integers):
#     return integers[0]
#
# class Integer:
#     def _init_(self, val):
#         self.val = val
#
#     def __gt__(self, other):
#         return self.val > other.val
#
#
#
# i1 = Integer(3);
# i2 = Integer(4);
# print(i1.val)
# # integers = [Integer(3), Integer(2), Integer(1)]
#
# # integers.sort()
#
class Integer:
    def __init__(self,val):
        self.val = val

    def __gt__(self, other):
        return self.val>other.val


integers = [Integer(3),Integer(2),Integer(1)]

integers.sort()
print(integers[0].__str__())




