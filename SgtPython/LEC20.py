#KEYWORD ARGUMENT KE BADD POSITIONAL ARGUMENT NOT ALLOWED
#DEFAULT KE BADD NON DEFAULT NOT ALLOWED
"""
def hello(a=5,b=6,c=7):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("Method 2")
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")
print(hello.__defaults__)#(5,6,7)
hello()
def abc():
    print("ABc was called")
    return 5
#prove that defaults are with definition
def hellos(a=abc()):

    print("2")

op: "Abc is called"
hellos()
hellos()
hellos(3)
op:1 2 2 2 because a ais already evaluated once


position only arguments:
def complicated(a,b,c/d = 5):
 return a+b+c
before slash position and after kuch bhi
print(add(4,2,11,d=5))

variable length argument:
print(1,2,3,4,5,6,7,8,9)
they accept as much arguments but inreality it combined together to form a tuple
and then they are passed as arguments in print:converting arguments into tuple called as vargs variable length argument
def print(value)

def add(a,b):
    a+b
we want to add three nos 5+7+10
add(5,7)
if we want to pass n arguments
then
def add(*args):
    sum = 0
    for num in args:
        sum+=num
    return sum

print(add(12,3,4))
type of args as tuple
if there are different parameter than
if we want to write after args then we will use keyword argument
def add(*args,operation):
    sum = 0
    for num in args:
        sum+=num
    return sum

print(add(12,3,4,"add")) show the error
print(add(12,3,4,operation = "add")) will work
print(add("add",12,3,4,))if add(operation,*args) then it will work
print(add(12,3,4,operation = "add",5)) will not work postion not allowed after keyword
* is mandatory
nums=[1,2,3,4]
calculate (nums,operation ="add") it will print((1,2,3,4)]
if we write calculate(*nums,operation = "add") op: (1,2,3,4)
if we want to pass collection in args then we have to write(*collection_name)

"""
"""
Anonymous function:
def based_on_custom(el):
    return len(el)
list =["f","s","t"]
lst.sort(key = based_on_custom)S
small funtions
used only at a certain place
give more idea about the working of it ,in the same line itself
lambda: a,b,c: sum(a,b,c)

"""
"""
map()
filter()
reduce()
map:
changes the quality
does not change the quantity
filter:
changes the quantity
does not change the quality
reduce:
takes a collection and reduces it to a small form 
eg:
1 2 3 4 5 6 7 6
Map:
def square(element):
    return element**2
numbers = [1,2,3]
result = map(square,numbers)
for res in result:
    print(res)
"""