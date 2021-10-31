"""
Sets:
Colection of elements with no duplicates
unordered collection of elements woth no dupicates are called as set
unordered (no indexing) collection of immutable objects
unchangeable
A collection of elemeents where searching can be done in O(1)
Properties of set:
No duplicates
Cannot sort a set
No indexing
Mutable
Unordered
Uses Hashing
Can insert only hashable elements
No indexing because of hashing
if we change the element mutable than its hash value changes which will create a problem in search thats why
elements are immutable in set
set is unordered therefore no sorting
no duplicates obvious hashing
"hello" can be stored in set len(5) but we have to covert into int then hash function get index and store it at that index
4-- no conversion and rest all same
(1,2,3) convert to integer value sum =6 apply hash function and store at that index
(1,2,3)
set does not allow list because of mutability and it will not do proper hashing
print(hash('hello')) gives random hash value
print(hash([1,2,3]):unhashable list:list cannot be hashed because of mutability of list
if i want to hash some object then that object can be stored in set



Testing:
set_1 ={}
print(type(set_1)) it will give dict
if set:
set_1 = set()
it will ignore duplicates
my_list = [1,2,3,4,5]
my_string  = 'hello'
my_tuple = (1,2)
set1={1,2,3,my_string} will work
set1={1,2,3,my_tuple} will work
set1={1,2,3,my_list} will not work
if my_tuple =(1,3,my_list)
set1={1,2,3,my_tuple} will not work
if tuple contains list anywhere then it will not add in set
set does not contain:
list
set
dict
and tuple with list



set_1 = {11,8,6,15,0}
print(set_1)
the order will be differenet order
myset ={10,13,8,16}
10-->10%8=2
13-->13%8 =5
8->8->0
16-->16-->0 index1
if(n>1 &n<4):
hshfunction %8:Divison method+linear probing
0 8
1 16
2 10
5 13
n>=5 till n<??
hash function linear probing using%32
mysset ={14,19,23,32,64}
14%32 = 14
19%32 = 19
23%32 = 23
32%32 = 0
64%32 = 1
{32,64,14,19,23}
n is the length of set







"""

"""
Set operations:
add() if we add add duplicate then it will not affect anything
clear : clear the set
copy copy the current set into new one
discard(element) delete the element if present
pop() removes random variable and rasies an exception if empty
remove(elem): if elem is not present then it will show error
set1.update(set2):set1{1,3},set2={2,5}
set1 = {1,3,2,5}
list =[3,4]
set1.update(list) because it have the collection
if list1[1,[2,3]]: wont update
set is not hashable datatype  but elements are hashable
Sort a Set
set = {1,2}
sorted = sorted(set)69*
"""
"""
Lec17:

class Something:
        def __init__(self,val):
            self.val = val
s1 = something(4)
s2 = something(5)
my_objects = {s1,s2}
print(my_objects}
"""
