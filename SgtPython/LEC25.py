# class Living:
#     def __init__(self):
#         print("I am a living")
#
# class Student:
#         __slots__ = {"name","age","marks"}
#         def __init__(self,name,age,marks):
#             self.name = name
#             self.age = age
#             self.marks = marks
#
#
# s1 = Student("Khushboo",19,98)
# print(s1.__dict__)
#
# # so basically slots are used  to make multiple dictionary for other objects
#
#
#     # Inheritance:
#     # super("Kiska parent call karna hain","reference").methodname(parameters)
#
#
#     class Animal:
#         def __init__(self, breed):
#             self.breed = breed
#
#         def sleep(self):
#             print("Zzzzz")
#
#
#     class Dog(Animal):
#         def bark(self):
#             print("Bow bow")
#
#      d = Dog()