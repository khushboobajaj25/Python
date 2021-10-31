"""
filter remove something
and accept something

"1 2 3 4 5 6"
[1,2,3,4,5,6]
numbers =[int(x) for x in input("enter nos").split()]
int(x):act as map(for ke phele)
numbers =[int(x) for x in input("eneter nos").split()filter if ]
filter after for loop
"""
"""
input ="1 2 3 4 5"
string
list of string 
even_numbers = [int(x)for x in input("Enter even numbers").split() if int(x)%2 ==0 #filter]
print(even_numbers)
1.take list of integers as input and store the power(raise to 2)to each number
powers = [int(num)**2for num in input("Enter a number").split()]
print(powers)
2.sum of two list in another list
first = [1,2,3,4,5]
second = [2,4,5,6,7]
z = [x+y for x in first for y in second]
print (z)
2:
words_in_set = set( input("Enter words").split())
words_in_list = input("Enter string").split()
result =[x for x in words_in_list if x is not words_in_set]
print(result)
3.Input a list of integers and print only odd nos
number = [int(num) for num in input("enter odd nos").split()if int(num)%2!=0]
print (number)
4.Take nos and do square of even nos and keep odd nos as it is
l = [int(x) if int(x)%2!=0 else int(x)**2for x in input("Enter numbers").split()]
print(l)
5:Do square of even numbers and discard odd nos
l =[ int(x)**2 for x in input("Enter nos").split() if ( True if int(x)%2==0 else False)]
print(l)
6:square of even and cube of odd
l = [int(x)**3 if int(x)%2!=0 else int(x)**2for x in input("Enter numbers").split()]
print(l)
7.vowels in string
vowels = "aeiou"//instead of keeping string keep it in set forO(1)searching
vowels={a,e,i,o,u}
vowels_in_input =[x for x in input("Enter a string") if x in vowels)
print(vowels_in_input)



Tuple Unpacking 
x,y,z = val
Tuple Packing
x
"""
nums = (int(x) for x in input("Enter nos").split())
#generator generates only when required
# GENERATES
