"""These comments are called multiline strings
id for int changes
but for True,False,None same id
str=> "hello" "hello"--same id(but changeable)(id differnt when given in input)
compile time:
x = 500,y=500(smae object same id)
run time:
x = "hello"
y = input() input ="hello"
a =input() input = hello
b = input() input = "hello
if it will search the same string then it take will time it will not create new object again and again
this concept is called string interning applicable for immutable.
x=[1,2,3]
y =[1,2,3]
print(id(x))//id different because mutable
print(id(y))//id different because mutable
this will happen in compile and run time
tuple has same id because immutable is called "string interning"
==--> checks for value
is-->checks for reference-->compares id for two variables
is-> is is a keyword that calls the function
x="hello"
y="hello"
print(x==y)
print(x is y)
both will give true in compile time
and different in run time
for list:
x=[1,2,3]
y = [1,2,3]
print(x==y)values same(true)
print(xisy) refernece differnet (false)

class SGT:
    def ----init---(self,x):
range is a constructor of class range
int = 4bytes
range =4(dynamically allocate memory)

"""

a = 56.4
b = float("56.4")
c = 50.2
d = 6.2
e = c+d
f = float(c)+float(d)
print(id(a))
print(id(e))
x = 5
y = 2+3  # ids are same because it adds two numbers and they are not assigned to variables it is called as literals(x,y)

