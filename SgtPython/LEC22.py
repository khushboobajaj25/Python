"""
Classes And Objects:
class:
Related Things together
Reusability
Access modifiers(public,private,default,protected)


Object
Multiple objects can be created out of 1 class
Instance methods behar se nahi access kar sakte
Objects are created using constructors

OOpm
Abstaraction

"""
"""
class Student:
    constructor is init
    init is initialser
    
    if we want to define  variables
    def __init__(self,name,rollNo)
        print()
s = Student()
print(s)
variables are called as field / attributes/methods
methods
class Student:
    def __init__(self,name,age, address, std="X",roll_no=0):
        print("Constructor Called")
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.address = address
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

    def print_details(self):
        print(self.name,self.roll_no)
    def random(self):
        print("Hey there")
s = Student("khushi",18,"1234","Mba",6)
print(s.is_adult())
print(s.print_details())
s.print_details()
Student.print_details()
#same thingl
#object s.function_name(s) will work likke this

"""






"""
wap to create simple student class roll no should be autoasign
"""
# class Student:
#     rollno= 1
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.Rollno = Student.rollno
#         Student.rollno+=1
#     def roll_no(self):
#         print(self.rollno)
#
#
# s = Student("Khushi",18)
#
# s1 = Student("Disha",17)
# s.roll_no()
# s1.roll_no()
#
def based_on_k_element(elem):
    return elem[k]


n = [int(x) for x in input().split()]

result = []
for i in range(n[0]):
    lst = []

    for j in range(n[1]):
        x = int(input())
        print(x)

        lst.append(x)

    result.append(lst)
k = int(input())

res = sorted(result, key=based_on_k_element)
for i in range(len(res)):
    print(res[i])
    print()



