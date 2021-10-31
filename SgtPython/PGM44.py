integers = list(range(1,11))
print(integers)
odd = list(range(3,16,2))
"""
if wwe use [range (3,16,2)] it will print excact range function 
"""
print(odd)
lst = "hello-hi-bye"
c = " -".join(lst)
print(c)

#part c

set_int = set()
se_char = set()
#parta
#byte:store values from 0 to 255
#ByteArray:values from 0to 255
#they store string s unicode values
"""
If we have to create a mutable string forcefully in python?
we will use byte array strings store bytearray internally
"""
list = [int (x) for x in input("Enter squence from 0 to 256").split() if(x>=0 and x<=255)]
byte_int = bytearray(list)
print(byte_int)