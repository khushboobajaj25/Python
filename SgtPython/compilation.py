"""Run:python file.py
Compile:python -m py_compile file.py
Check bytecode : python -mdis file.py
data types in python:
Atomic:(immutable object)
bool int float complex None
m mutable
i  immutable
Collection:
Ordered : str(i) byte(i) bytearray(m) list (m)tuple(i)
Unordered : set(m) frozenset(i)
Map : dict(m)
default package python builtins
every object has unique id
Immutable object : if you want to change me create a new object
eg tuple ,frozen set,str,int,bool,float complex,None,
eg strings value and address remains the same
Mutable object
eg list ,set ,dict,array
update the value of the object and keeping the address same

 input function: input() always return string
 print ()

 boolean ==> 0
 0.0
 False
 None
  empty list,tuple
  int 0,
  float 0.0
  bool false
  str =""
  example:



"""
x = True
y = True
print(id(x))
print(id(y))
"""x = 123
print(id(x))
print(type(x))
x = 7
print(id(x))
x = input()
print(x)
y ="0123456789"
z ="d"
print(id(y))
print(id(z))
x = 1.0
y = float(input())
print(id(x))
print(id(y))
"""
