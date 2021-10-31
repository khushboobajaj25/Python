"""
Walrus operator 3.8+(:=):
assignment
expressions

print(greeting := input("enter a string"))
if (day := input("Enter a day") )== Staurday
    print("weekend")
else:
    print("study time")
print("the day is",day)

students = []
while(sgt_student:=input("Enter a name"))!="Vinay"
        students.append(sgt_student)
else
        print("Vinay")
"""
"""
chp 5:
List
list si dynamic
every datatype
Mutable
List are represented using []
List class is list()
List can be accessed by indexing 
Tuple:
Immutable 
Represented using ()
Tuple can contain anything which is possible in python
Tuple class is tuple()

mylist [1,2,3]
t = (mylist,"abc","def")#([1,2,3],"abc","def")
mylist.append(4)
print(mylist)[1,2,3,4]
print(t)#([1,2,3,4],"abc","def")

Set:
dynamic 
mutable object 
Set class is set()
Indexing 
Contains anything except duplicate
Uses hashing
Cannot sort a set
Can do venn diagram operations
Searching is fast O(1)


Str:
Immutable
Contains charcters 
Represented using "
class name is str()
Indexing yes



input
x = input("Enter some name").split(",")(always return list,by default space,it does not allow"")
print(type(x))
sprint (x)
x = list(input("enter some name")
converts a input to a list
x =[(input("enter some name")]
converts a list into input 

"1 2 3 4 5"
numbers = input("Enter numbers").split()
for i in range (len(numbers))
        numbers[i] = int(numsbers[i])
print numbers

numbers = [int(num)for num in input("Enter some name").split()]
this is the input which will accept a string in list  and change that string in to integer and gets into list This is called
List Comprehension
But the above statment when converted into tuple like
(int(num)for num in input("Enter some name").split())
wont be allowed because list comprehension does not allow ()
split function always give the list

z=[x for x in input("Enter strings")]
"abc def xyz"



tple = (1,2,3)//tuple
print(tple)
print(type(tple))


tple(1)//not a tuple type:int if we want a tuple then write("abc",)
print(tple)
print(type(tple))





"""
t = (1,"k",2,False)
z=[x for x in input("Enter strings") if x!=" "]
print(z)
