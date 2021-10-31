"""
FORMING A DICTIONARY FROM STRINGS
s = "Watch=4000,Jeans=6000,Shirt=4500,Shoes=5500"
for x in s.split(","):
    y = x.split("=")
    lst.append(y)
Until3.5 dictionary were not ordered To use the ordered dictiom-nary we had a class collection package
in  3.6 we have ordered dict
entries = {"Anisha":18,""Karan":61,"Khushboo":06}
print(sorted(entries.values()))
def based_on_roll_no(record):
    return record[1]
record of datatype is tuple
result = dict(sorted(entries.items(),key = based_on_roll_no))a
max funtion
min func:
zip func:
list1={1,2,3}
tple=(2,3,5)
list2 = {"one","two"}
it will gorup the ith element of all and form tuple
result = zip(list_1,list_2,tuple)
op:
(1,2,one)
(2,3,two)

"""
"""
Functions:
function has id
type function
def  foo(name,roll,marks=40):
    print(name)
    print(roll)
    print(marks)
foo("ajk",25)
if we does not want any argument make your parameter with default value
if i do like this
foo(1,"ritesh",25)
then ordering change hojayega
if we print ordering will change
foo(name = "ritesh",roll no =1,marks =25) this is called keyword argument
foo(rollno =2,"ritesh",25) this wont work
foo(1,marks = 122,name ="xyz")thisis will works
foo(roll=12,name = 122,100)
thiswont work
function can be passsed to another function
def foo(bar)
    bar()
def hello():
    print("hello")
foo(hello)
A function cannot return multiple values:but we can do it by storing in tuple
def calculator(a,b):
    add = a+b
    mul = a*b
    sub = a-b
    div = a/b
    return add,sub,mul,div
a,s,m,d = calculator(4,2) it is not returning many values it return one value by tuple unpacking we can do but function does not return many values
    variable length argument:
    
    def foo(first:str,second:str,result:list)
        result.append(first)
        result.append(second)
        
animals[]
foo("horse","cat",animals)
if we return result it will not make any change
if we does no have animals
 def foo(first:str,second:str,result=list())
        result.append(first)
        result.append(second)1  
birds = foo("horse","cat")
print(birds)
plants = foo("Neem","Cactus")
print(plants)
op:
["horse","cat","Neem","Cactus"]
if we write  again this:
animals[]
foo("horse","cat",animals)
toh same output dega
default values in function parameters evaluate one time
default values in funtion parameters are with function definition not with function calls

Is this behaviour good?//it helps to save memory and working
what advantage is giving it in python?
Any good application
If i don't want this what should i change?

    
"""


