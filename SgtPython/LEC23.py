# # # Class Variables:
# # # Created Once
# # # Can be called using Classvariables
# # # Can also be called using self.variable
# # # Search preference is first in self then in class
# # #
# # # Class Methods:
# # # Pla y around class variables
# # # These are also used as constructors in some cases
# # # Static methods:
# # # Self and class not required
# # # They can be copy pasted into another classmethod
# # # They are also called helper methods
# # # intra class binding
# # # inter class binding
# # #so if we write multiline comments after init the dictionary with key doc will display comments
# #
# # class Sample:
# #     foo = 5
# #
# #     @classmethod
# #     def foo(cls):
# #         return "hello World"
# # print(Sample.foo)#reference
# # print(Sample.foo())#functiondefn
# #
# # class Sample:
# #     foo = 5
# #     @classmethod
# #     def foo(cls):
# #         return "hello World"
# # B.__init__(self,name)
# #
# #
# #
# #
# # print(Sample.foo)#reference
# # print(Sample.foo())#functiondefn
# # s = Sample()
# # print(s.__dict__)
# #
# # _var single underscore:when you wantto represent private fields
# # _marks
# # s1.marks karenge toh it will not field it will create private member
# # if we want to print that marks so awe will write s1._marks
# #
# # var_-->underscore after
# #
# # marks = 100
# # marks_ to avoid same names
# # __var double underscore
# when you want to use private fields
# we will write
# s1._ClassName.__marks this is called name mangling

# # __var__ dunder: should not use this