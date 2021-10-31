sentence = "ababHelloworld helloab"
print(sentence.lstrip("ab"))
sentence ="ababHello world"
print(sentence.removeprefix("abab"))
print(sentence.removesuffix("Hello world"))
"""
imutable   mutable
string     list
            sort() only sort list
to sort
sorted()
new collection= sorted(collection)
sorted(string,reverse - true) gives you desecnding and false give you ascending
sorted() always return list  if we want string then we have to type caste string
but it will not typecast string 
becausse list in string will give you stringg
therefore we will use join method
1.why strings are immutable?what diff woild it make if strings are mutable

2.what sorting algorithim is applied in.sort() and sorted() methods?and why?

"""
"""
LISTS:
def foo():
    return 5

class Confusion:
    defC   self.a =5

sample_list = [23,34,55,Confusion,foo]
print(sample_list)
c = Confusion()# create object
c = sample_list[3]()# creating an object of Confusion which is sample_list[3]
print(type(c))
print(sample_list[4]())#call a function foo which is sample_list [4]
print(id(Confusion))

Creating a list:
lists =  range(2,30,2)
list_of_evennos = list(lists)
print(list_of_evennos)
functions:

del
reverse
append function always always increases by length 1
extend():always take any iterable like list and set 


"""




