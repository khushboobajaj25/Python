list1 = [1,2,3,4]
list2 = list1
list1.append(5)
print(list1)
print(list2)
"""
list are mutable is call by reference
max min in builtins.py
max and min should be comparable
 a,*b = [1,2,3,4,5,6]
 * arg variable length arguments the remaining will assign to this argument
 a,*e = [] does not work
 
 a = 1
 b = [2,3,4,5,6]
 
 """
a = [1,2,3]
b = [[4,5,6]]
a.extend(b)
print(a)